import os
import time
import psutil
import string
import random

hardware_info = {
    "os": os.name,
    "cpu_cores": psutil.cpu_count(logical=False),
}


# menu 1
def get_system_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")

    print("Загрузка информации об операционной системе..")
    time.sleep(random.uniform(1.344, 2.0111)) 

    print("\nИнформация об операционной системе: ")
    print(f"Процессор загружен на: {cpu_usage}%")
    print(f"Оперативная память: {memory.percent}% использовано")
    print(f"Свободно на диске C: {disk.free // (2**30)} ГБ")


# menu 2
def kill_process():
    target = input(
        "Введите имя процесса для закрытия (например, chrome.exe): "
    ).lower()
    found = False

    print("Загрузка всех процессов..")
    time.sleep(random.uniform(1.4, 2.11))

    print("Завершаю процесс")
    time.sleep(random.uniform(0.8, 1.888))

    for proc in psutil.process_iter(["name"]):
        try:
            if proc.info["name"] and proc.info["name"].lower() == target:
                proc.terminate()
                found = True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if found:
        print(f"Все процессы '{target}' успешно завершены.")
    else:
        print(f"Процесс '{target}' не найден среди запущенных.")


def main():
    print("CLI-Ассистент запущен. Введите команду (или 'выход')")
    print("См. раздел `помощь`")

    while True:
        command = input("\n>>> ").strip().lower()

        if command == "выход":
            print("Завершение работы программы...")
            time.sleep(random.uniform(0.8, 1.856))
            break

        elif command == "система":

            print("Загрузка раздела `система` ... ")
            time.sleep(1)
            get_system_status()

        elif command == "процесс":

            print("Загрузка раздела `процесс` ... ")
            time.sleep(1)
            kill_process()

        elif command == "автор":

            print("Автор Fassydev")
            print("Github - http://github.com/fassy-dev")

        elif command == "помощь":

            print("Загрузка раздела `помощь` ... ")
            time.sleep(random.uniform(0.8, 1.8))

            print("Все команды:")
            print("система - Информация об операционной системе")
            print("процесс - Меню для закрытия процесса")
            print("автор - Меню автора проекта")
            print("выход - Выключение данной программы")
            print("помощь - Данный раздел")

        else:
            print(
                "Неизвестная команда. Попробуйте 'система', 'процессc, 'помощь' или 'выход'.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nЗавершение работы программы...")
