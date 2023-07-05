# -*- coding: utf-8 -*-
"""
Завдання 15.1b

Перевірити роботу функції get_ip_from_cfg із завдання 15.1a на конфігурації
config_r2.txt.

Зверніть увагу, що на інтерфейсі e0/1 призначено дві IP-адреси:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary


А у словнику, який повертає функція get_ip_from_cfg, інтерфейсу Ethernet0/1
відповідає лише один із них.

Копіювати функцію get_ip_from_cfg із завдання 15.1a та переробити її таким
чином, щоб у значенні словника вона повертала список кортежів для кожного
інтерфейсу. Якщо на інтерфейсі призначено лише одну адресу, у списку буде один
кортеж. Якщо на інтерфейсі налаштовані кілька IP-адрес, то списку буде кілька
кортежів. Ключем залишається ім'я інтерфейсу.

До словника додавати лише ті інтерфейси, на яких налаштовані IP-адреси.

Перевірте функцію конфігурації config_r2.txt і переконайтеся, що інтерфейсу
Ethernet0/1 відповідає список з двох кортежів.

Зверніть увагу, що в даному випадку можна не перевіряти коректність IP-адреси,
діапазони адрес і так далі, оскільки обробляється вивід команди, а не введення
користувача.

Приклад виклику функції
In [8]: pprint(get_ip_from_cfg("config_r2.txt"), sort_dicts=False)
{'Loopback0': [('10.2.2.2', '255.255.255.255')],
 'Ethernet0/0': [('10.0.23.2', '255.255.255.0')],
 'Ethernet0/1': [('10.255.2.2', '255.255.255.0'),
                 ('10.254.2.2', '255.255.255.0')],
 'Ethernet0/2': [('10.0.29.2', '255.255.255.0')]}

"""
