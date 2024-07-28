"""
This version maintains continuity of conversation by including chat history
in each new API call.
"""
from openai import OpenAI

client = OpenAI(api_key="YOUR-API-KEY")

print("Welcome to ChatGPT! Type 'quit', 'exit', or 'bye' to end the conversation.")
# include the AI's area of expertise, will be the first item in every API call
ai_specialization = input("What is my area of expertise? ")
system_prompt = {'role': 'system', 'content': 'You are a '+ ai_specialization}
# keep track of conversation to include with each API call
chat_history = []
while True:
    # ask user question
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
    # keep responses succinct to limit token usage
    user_input = user_input + "Please keep your response to 50 words or fewer."
    # append to chat history
    chat_history.append({'role': 'user', 'content': user_input })
    # start messages dict list with area of expertise and add recent chat history
    messages = [system_prompt]
    messages.extend(chat_history)
    # send request to API
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    # add response to chat history and remove oldest items
    response = completion.choices[0].message.content.strip()
    chat_history.append({'role':'assistant','content': response})
    chat_history = chat_history[-10:]
#     for message in messages:
#         print(message)
    # display response
    print(completion.choices[0].message.content.strip())
