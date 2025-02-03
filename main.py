from flask import Flask
from flask import render_template,request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import AutoTokenizer, AutoModelForCausalLM
from application.database import *
import re
from sqlalchemy import text

model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto",offload_folder="offload")

def translate_to_sql_select(english_query):
    input_text = f"""
        Given the following database schema:
        **Employees Table**:
        - id 
        - name
        - department
        - salary 
        - hire_date 
        **Departments Table**:
        - id 
        - name 
        - manager
        {english_query}
        Convert this English text into an SQL query.
        """
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200)
    pre_final = tokenizer.decode(outputs[0], skip_special_tokens=True)
    try:
        final = re.search(r'```sql\n(.*?)\n```', pre_final, re.DOTALL).group(1)
    except:
        final = "Sorry, Unable to convert the given query to SQL. Try again with a different query."

    return final

def query_to_string(query_result):
    if query_result:
        columns = query_result[0].keys()  
        rows_as_string = "\n".join(
            [", ".join([f"{col}: {row[col]}" for col in columns]) for row in query_result]
        )
        return rows_as_string
    else:
        return "No results found."


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.sqlite3'
db.init_app(app)
app.app_context().push()

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        user_query = request.form.get('input')
        sql_query = translate_to_sql_select(user_query)

        sql = text(sql_query)
        result = db.session.execute(sql)  # Use parameters to prevent SQL injection
        users = result.fetchall()

        users_str = query_to_string(users)
        
        return render_template('index.html',text=users_str)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)