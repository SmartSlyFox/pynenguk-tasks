"""
Запросити користувача введення кольору через input.

Якщо введений колір є у списку colors, вивести повідомлення "Такий колір є".
Якщо немає кольору, вивести повідомлення "У списку colors немає такого кольору".

Зробити так, щоб користувач міг вводити колір у будь-якому регістрі, але при
цьому перевірка для слова працювала (нижче приклад).


Приклад роботи завдання
$ python task_11.py
Введіть колір: red
Такий колір є

$ python task_11.py
Введіть колір: Red
Такий колір є

$ python task_11.py
Введіть колір: RED
Такий колір є

$ python task_11.py
Введіть колір: blue
У списку colors немає такого кольору

При цьому не можна змінювати список colors.
"""
colors = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']

