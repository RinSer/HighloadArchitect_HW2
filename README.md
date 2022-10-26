## Инструкция для запуска:

1) Установить Docker и python 3.8
2) Выполнить в текущей директории CLI команду `docker-compose -f db.yml up` для запуска базы данных.
3) Выполнить в текущей директории CLI команду `py -3 -m pip install -r requirements.txt` для установки зависимостей приложения.
4) Выполнить в текущей директории CLI команду `py -3 -m flask --app app run` для локального запуска приложения (порт 5000).

Обновить requirements.txt: `py -3 -m  pipreqs.pipreqs --force`