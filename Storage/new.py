import requests


def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"

    # Выполняем GET-запрос
    response = requests.get(url)

    # Проверка статуса ответа
    assert (
        response.status_code == 200
    ), f"Expected status code 200, but got {response.status_code}"

    # Проверка, что ответ является JSON
    assert (
        response.headers["Content-Type"] == "application/json; charset=utf-8"
    ), "Response is not JSON"

    # Проверка количества пользователей
    users = response.json()
    assert len(users) > 0, "No users found"


if __name__ == "__main__":
    test_get_users()
    print("All tests passed!")
