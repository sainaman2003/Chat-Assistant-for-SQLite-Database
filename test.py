from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Ellbendls/Qwen-2.5-3b-Text_to_SQL")
model = AutoModelForCausalLM.from_pretrained("Ellbendls/Qwen-2.5-3b-Text_to_SQL")

# Input prompt
query = "Show me all employees in the Sales department."

# Tokenize input and generate output
inputs = tokenizer(query, return_tensors="pt")
outputs = model.generate(**inputs, max_length=512)

# Decode and print
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
print(outputs)
