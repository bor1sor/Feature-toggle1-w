import time

seconds = int(input("Введите количество секунд: "))

for i in range(seconds):
    print(str(seconds - i) + " секунд осталось")
    time.sleep(1)

print("Время вышло!")
