# AI API Integration

This assignment is about using different AI APIs in Python.

I created separate Python files for each API and tested how they respond to user input.

## APIs used

* Groq API
* Cohere API
* HuggingFace (using transformers locally)
* Ollama (running locally)

## What I did

* Took user input from terminal
* Sent it to different AI APIs
* Displayed the response
* Handled basic errors
* Used environment variables instead of hardcoding API keys

## How to run

1. Create virtual environment
   python -m venv 
   venv\Scripts\activate

2. Install required packages
   pip install -r requirements.txt

3. Create a `.env` file and add your keys
   GROQ_API_KEY=your_key
   COHERE_API_KEY=your_key
   HF_API_KEY=your_key

4. Run the files
   python groq_api.py
   python cohere_api.py
   python hf_api.py
   python ollama_api.py

For Ollama, make sure it is running in another terminal using:
ollama serve

## About API keys

API keys are not included in the project for security reasons.

I used a `.env` file to store keys locally and did not upload it to GitHub.

A `.env.example` file is added to show how to add the keys.

## Student Name

Dhushyanth G S
