import json
import requests

# Чтение объекта из JSON файла
with open('example_request.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# URL для POST запроса
url = 'http://127.0.0.1:5000/get_object'  # замените на необходимый URL

# Отправка POST запроса с данными
response = requests.post(url, json=data)

# Проверка ответа
if response.status_code == 200:
    print("Данные успешно отправлены")
    print(f"Ответ сервера: {response.text}")
    with open('example_responce.json', 'w') as json_file:
        json.dump(response.text, json_file, indent=4)
else:
    print(f"Произошла ошибка: {response.status_code}")
