# Chat with GPT-3.5 in your python terminal

This is a simple script that lets you interact with OpenAI's GPT-3.5 model. You can ask questions or have a conversation with the AI.

## Setup

1. **API Key**: Before you can use this script, you'll need an API key from OpenAI. If you don't have one, sign up at [OpenAI](https://platform.openai.com/signup) and get your key.

2. **Environment Variable**: It's a best practice not to hardcode your API key in the script. It's recommended to set it as an environment variable. However, the current script contains a placeholder for the key. If you choose to use the hardcoded method, replace the placeholder in the script with your actual key.

3. **Dependencies**: The script requires the `openai` Python library. Install it using pip:
   ```bash
   pip install openai
   ```

## Usage

1. **Running the Script**: Navigate to the directory containing the script and run:
   ```bash
   python main.py
   ```

2. **Interacting**: After running the script, you'll see a prompt `Ramsey:`. You can type in any message or question and press enter.

3. **Exiting**: To exit the chat, simply type `quit`, `exit`, or `bye` when prompted.

## Error Handling

The script includes basic error handling for rate-limiting. If you exceed the number of API calls allowed by your OpenAI plan, you'll receive a message indicating that the limit has been reached.

---
