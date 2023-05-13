import json
import requests


def talkgpt(content):
    url = "https://api.openai.com/v1/chat/completions"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{content}. write 100 word"}],
        "temperature": 1.0,
        "top_p": 1.0,
        "n": 1,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {'API KEY '}"#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
    }

    response = requests.post(url, headers=headers, json=payload, stream=False)

    result = response.json()


    with open('text.json', 'w') as file:
        json.dump(result, file, indent=4)

    return f"AI: {result['choices'][0]['message']['content']}"


