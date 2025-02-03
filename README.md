# SQL Query Generator using AI Assistant

This project is a Flask web application that leverages an AI model to convert natural language queries into SQL queries. The assistant uses a pre-trained model (`DeepSeek-R1-Distill-Qwen-1.5B`) from Hugging Face to understand English text and generate SQL queries for a database containing employee and department information.

## How the Assistant Works

1. **Input**: The user provides an English-language query via the web interface.
2. **Processing**: The query is passed to the Hugging Face model, which generates an SQL query based on the schema of the `Employees` and `Departments` tables.
3. **Output**: The AI-generated SQL query is executed against an SQLite database, and the results are displayed on the webpage.

### Tables in the Database:
- **Employees Table**: Contains columns `id`, `name`, `department`, `salary`, and `hire_date`.
- **Departments Table**: Contains columns `id`, `name`, and `manager`.

## Steps to Run the Project Locally

### Prerequisites:
Make sure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

### 1. Clone the repository 
Clone this repository to your local machine:

https://github.com/sainaman2003/Chat-Assistant-for-SQLite-Database.git
pip install -r requirements.txt
python app.py

##Limitations

- **High Computational Resources**: The model requires significant computational resources and may take a long time to provide results.
- **Performance**: Query generation and execution might be slow for larger models or complex queries.

## Suggestions for Improvement

- **Model Optimization**: Optimize the model to reduce resource consumption and improve response time.
- **Cloud Deployment**: Consider deploying the model on cloud services with better computational power to handle large queries efficiently.

## Hugging Face Deployment

You can also access the model on Hugging Face [here](https://huggingface.co/spaces/sainaman/Sai-Naman-Chat-Assistant-for-SQLite-Database) for testing or deployment in other applications.




