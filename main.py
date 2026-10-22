"""
This version maintains continuity of conversation by including chat history
in each new API call.
"""
from ollama import chat
from ollama import ChatResponse

system_prompt = {'role': 'system', 'content': 'You are a helpful assistant.'}
# keep track of conversation to include with each chat call
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
    # start messages dictionary list with system prompt and add recent chat history
    messages = [system_prompt]
    messages.extend(chat_history)
    # send request to chat
    response: ChatResponse = chat(
        model='gemma3:2b',
        messages=messages,
    )
    # add response to chat history and remove oldest items
    response = response.choices[0].message.content.strip()
    chat_history.append({'role':'assistant','content': response})
    chat_history = chat_history[-10:]
#     for message in messages:
#         print(message)
    # display response
    print(response['message']['content'])
"""
response: ChatResponse = chat(
  model='gemma3:latest',
  messages=[
    {
        'role': 'system',
        'content': 'You are a helpful assistant.',
    },
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
  ],
)
print(response['message']['content'])
"""
