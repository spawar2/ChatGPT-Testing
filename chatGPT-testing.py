# "OpenAI's GPT-3/ChatGPT: Suggests, but not Corrects"
# Built-in Functions: https://www.programiz.com/python-programming/methods
import os
import time
from datetime import datetime
import openai

os.chdir("./")
sleep_interval = 10
open_ai_key = "OPENAI_API_KEY"

# Initialize the API key for OpenAI
if open_ai_key in os.environ:
    openai.api_key = os.environ[open_ai_key]
else: 
    raise ValueError(f"{open_ai_key} is not set in the environment.")


def get_chatgpt_response(question):

    completions = openai.Completion.create(
        engine = "code-cushman-001",
        prompt = question,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.2
    )

    return completions.choices[0].text


def read_py_files_in_folder():

    current_folder = os.getcwd()
    
    questions_folder = os.path.join(current_folder,"questions")

    responses_folder = os.path.join(current_folder,"responses")

    questions_folder_exists = os.path.exists(questions_folder)

    response_folder_exists = os.path.exists(responses_folder)

    if not questions_folder_exists:
        os.makedirs(questions_folder)

    if not response_folder_exists:
        os.makedirs(responses_folder)

    python_files = [f for f in os.listdir(questions_folder) if f.endswith('.py')]
    
    response_file = f"response-{datetime.now().isoformat()}.txt"
    
    with open(responses_folder + "/" + response_file,"a") as append_file:
        
        for python_file in python_files:
            
            print(f"Processing... {python_file}")
                    
            with open(questions_folder + "/" + python_file, "r") as file:
                
                code = file.read()

                question = f"Fix following Python code:\n\n{code}"
                
                response = get_chatgpt_response(question)
                
                content = f"\nQuestion:\n\n{question}\n\nResponse:\n\n{response}\n======="

            append_file.write(content)
            print(f"Done processing... {python_file}")
            time.sleep(sleep_interval)

    print("Finished")

if __name__ == '__main__':
    read_py_files_in_folder()
