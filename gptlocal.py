import requests
import json

def request_to_gpt(query):
    # URL для вашего локального API
    url = 'http://localhost:11434/api/generate'

    # Данные запроса
    data = {
        "model": "llama3.2",
        "prompt": query+"ответ не больше 900 символов и не используй латинские символы, и числа пиши не цифрами а прописью",
        "stream": False
    }
    # Отправка POST-запроса
    response = requests.post(url, json=data)

    # Проверка статуса ответа
    if response.status_code == 200:
        result = response.json()
        return (result['response'])
    else:
        return (f"Error: {response.status_code}, {response.text}")
