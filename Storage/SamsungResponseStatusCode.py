import requests

response = requests.get("https://www.samsung.com/ru/")
print(response.status_code)
