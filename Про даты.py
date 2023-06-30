import datetime
from dateutil.parser import parse  # py -3 -m pip install python-dateutil

d1 = datetime.date.today()  # фабрика, как random() у карты
d2 = datetime.date(2023, 1, 10)  # 10 января - обычный конструктор
d3 = datetime.datetime.strptime('20.05.2023', '%d.%m.%Y')  # тоже фабрика

print(d1, d2, d3)  # __str__()
print([d1, d2, d3])  # __repr__()

print(d1 > d2)  # __gt__()
print(d1 - d2)  # __sub__(), результат timedelta
print(d1 + datetime.timedelta(days=10))  # __add__(), результат - новая дата

print({d1, d2, d3})  # даты умеют хэшироваться
print(d1 == d2)  # __eq__()

# Парсим текстовые даты
# Есть метод datetime.datetime.strptime(), но ему нужно давать подсказку
# dateutil угадает сама
# объекты datetime, а не date
d4 = parse('23.04.2023')
d5 = parse('23/04/2023')
d6 = parse('01/04/2023')  # по умолчанию mm/dd/yyyy
d7 = parse('01/04/2023', dayfirst=True)  # дд.мм.гггг
d8 = parse('01 apr 2023')

d9 = d4.date()  # преобразовать в объект date

print(d4, d5, d6, d7, d8)

print(type(d4))
print(type(d9))
