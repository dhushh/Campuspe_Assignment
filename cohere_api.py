import os
from dotenv import load_dotenv
import cohere

# load env variables
load_dotenv()

# get api key
api_key = os.getenv("COHERE_API_KEY")

# create client
co = cohere.Client(api_key)

# function to get response
def get_response(prompt):
    try:
        response = co.chat(
            model="command-r7b-12-2024",   # correct latest model
            message=prompt
        )
        return response.text
    except Exception as e:
        return "Error: " + str(e)


# main
if __name__ == "__main__":
    user_input = input("Enter your prompt: ")

    result = get_response(user_input)

    print("\nResponse:")
    print(result)