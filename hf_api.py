from transformers import pipeline

# load text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# function to generate response
def get_response(prompt):
    try:
        result = generator(prompt, max_length=50, num_return_sequences=1)
        return result[0]["generated_text"]
    except Exception as e:
        return "Error: " + str(e)


# main program
if __name__ == "__main__":
    user_input = input("Enter your prompt: ")

    output = get_response(user_input)

    print("\nResponse:")
    print(output)