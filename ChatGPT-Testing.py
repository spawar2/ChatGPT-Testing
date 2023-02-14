# "OpenAI's GPT-3/ChatGPT: Suggests, but not Corrects"
# Built-in Functions: https://www.programiz.com/python-programming/methods
import openai
import os
os.chdir("/Users/pawar/Desktop/ChatGPT")
# Initialize the API key for OpenAI
openai.api_key = ""

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Read the questions from the text file
with open("questions.txt", "r") as file:
    questions = file.readlines()

# Remove leading/trailing whitespace from each question
questions = [question.strip() for question in questions]

# Make a query for each question and print the response
for question in questions:
    response = generate_response(question)
    print(f"Question: {question}")
    print(f"Response: {response}")
    print("-" * 1)
