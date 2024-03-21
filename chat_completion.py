from openai import OpenAI


def chat_completion(api_key):
    client = OpenAI(
        api_key=api_key
    )

    result = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[{"role": "user", "content": "안녕"}],
    )
    print(result.choices[0].message.content or '', end='')
    print('\nend of response')


def chat_completion_stream(api_key):
    client = OpenAI(
        api_key=api_key
    )

    result_stream = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[{"role": "user", "content": "안녕"}],
        stream=True
    )
    for stream in result_stream:
        print(stream.choices[0].delta.content or '', end='')
    print('\nend of response')
