import os
import django

# Установка настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skill.settings')
django.setup()

# После этого вы можете импортировать и использовать ваш код
from restapi.views import PerevalDataHandler

# Пример данных о перевале для добавления
data = {
    "beauty_title": "пер.",
    "title": "Пхия",
    "other_titles": "Триев",
    "connect": "",
    "add_time": "2021-09-22 13:18:13",
    "user": {
        "email": "qwerty@mail.ru",
        "fam": "Пупкин",
        "name": "Василий",
        "otc": "Иванович",
        "phone": "+7 555 55 55"
    },
    "coords": {
        "latitude": "45.3842",
        "longitude": "7.1525",
        "height": "1200"
    },
    "level": {
        "winter": "",
        "summer": "1А",
        "autumn": "1А",
        "spring": ""
    },
    "images": [
        {"data": "<картинка1>", "title": "Седловина"},
        {"data": "<картинка>", "title": "Подъем"}
    ]
}

# Создаем экземпляр класса PerevalDataHandler
handler = PerevalDataHandler()

# Добавляем данные о перевале в базу данных
result = handler.add_pereval(data)

# Выводим результат операции
print(result)
