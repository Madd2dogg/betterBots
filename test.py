from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set the pad token to the end-of-sequence (eos) token if it isn't set
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_name)

# Function to generate a response
def generate_response(prompt):
    # Encode the input prompt with attention mask and padding
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    
    # Generate the output using the model
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,  # Adjust max_length as needed
        pad_token_id=tokenizer.pad_token_id,  # Set the pad_token_id
        temperature=0.7
    )
    
    # Decode and return the output text
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def chat_loop():
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        # Generate and print the bot's response
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

# Start the chat loop
chat_loop()
