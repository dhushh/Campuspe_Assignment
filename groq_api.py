import os
from dotenv import load_dotenv
from groq import Groq

# load .env file from current directory
load_dotenv()

# get api key
api_key = os.getenv("GROQ_API_KEY")

# create groq client
client = Groq(api_key=api_key)

# function to get response
def get_response(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "Error: " + str(e)

# main
if __name__ == "__main__":
    user_input = input("Enter your prompt: ")

    result = get_response(user_input)

    print("\nResponse:")
    print(result)