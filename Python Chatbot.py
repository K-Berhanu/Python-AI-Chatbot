'''
import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role":"user","content":prompt}]
        )
    return response.choices[0].message.content.strip()
if __name__ == "__main__":
    while True:
        user_input = ("You: ")
        if user_input.lower() in ["quit","exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
'''
from openai import OpenAI

client = OpenAI(api_key="API KEY")
def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)

