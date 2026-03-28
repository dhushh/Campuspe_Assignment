import requests

# function to get response from ollama
def get_response(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        return data["response"]

    except Exception as e:
        return "Error: " + str(e)


# main
if __name__ == "__main__":
    user_input = input("Enter your prompt: ")

    result = get_response(user_input)

    print("\nResponse:")
    print(result)