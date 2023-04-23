import openai
def chat_with_gpt3():
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    
    print("Type 'quit' to exit the conversation.")
    while True:
        user_input = input("You: ")   
        if user_input.lower() == "quit":
            break
        messages.append({"role": "user", "content": user_input})       
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        assistant_message = response.choices[0].message["content"]
        print(f"Assistant: {assistant_message}")
        messages.append({"role": "assistant", "content": assistant_message})
def fail_linting():
    print("Fail")

if __name__ == "__main__":
    chat_with_gpt3()
