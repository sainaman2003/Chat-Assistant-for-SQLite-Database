from flask import Flask
from flask import render_template,request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import AutoTokenizer, AutoModelForCausalLM
from application.database import *

def load_model():
    model_name = "Qwen-2.5-3b-Text_to_SQL"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return model, tokenizer

def generate_sql(model, tokenizer, user_input):
    input_text =  f"translate English to SQL: {user_input}"
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(**inputs, max_length=150)
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql_query

app = Flask(__name__)
model, tokenizer = load_model()
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.sqlite3'
db.init_app(app)
app.app_context().push()


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        user_query = request.form.get('input')
        sql_query = generate_sql(model, tokenizer, user_query)
        return render_template('index.html',text=sql_query)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)