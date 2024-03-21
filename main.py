# Python 코드 예시
from dotenv import load_dotenv
import os
from chat_completion import chat_completion_stream, chat_completion
from openai import OpenAI

if __name__ == '__main__':
    # .env 파일 로드
    load_dotenv('config/local.env')

    # 환경 변수 불러오기
    api_key = os.getenv('OPENAI_PERSONAL_KEY')
    secret_token = os.getenv('OPENAI_PERSONAL_ORGANIZATION_ID')

    chat_completion(api_key)
    chat_completion_stream(api_key)
