import requests

url = "https://budu.ru/"
response = requests.get(url)

# Выводим заголовки
print(response.headers)
