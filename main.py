import openai

openai.api_key = ''  # https://platform.openai.com/account/api-keys


def chat_with_gpt(prompt):
    try:
        response = openai.Completion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )

        return response.choices[0].message.content.strip()

    except openai.error.RateLimitError:
        return "Sorry, I've exceeded my limit for now. Please try again later."


if __name__ == '__main__':
    while True:
        user_input = input('Ramsey: ')  # Name of your choice
        if user_input.lower() in ['quit', 'exit', 'bye']:  # keyword to quit
            break

        response = chat_with_gpt(user_input)
        print('Chatbot:', response)
