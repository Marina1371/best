a = [12, 34, 56, 34, 23, 67, 234, 678, 23, 67, 23, 67, 46]

# функция, которая даёт набор элементов списка, которые делятся на 2
def evens1(iterable):
    # return [x for x in iterable if x % 2 == 0]
    res = []
    for ai in iterable:
        if ai % 2 == 0:
            res.append(ai)
    return res

# минус в том, что мы составляем список целиком и храним его в памяти целиком
print(evens1(a))
for x in evens1(a):
    print(x)


# функция-генератор
def evens2(iterable):
    for ai in iterable:
        if ai % 2 == 0:
            yield ai  # вместо return


# Мы не составляем список целиком, то есть экономим место и распределяем нагрузку
# print(evens2(a))
# for x in evens2(a):
#     print(x)

# Этот объект одноразовый
gen = evens2(a)
for x in gen:
    print(x)

print('---')
for x in gen:
    print(x)

# Теперь про генераторы в одну строку

# генерит список
a1 = [x for x in a if x % 2 == 0]

# генерит множество
a2 = {x for x in a if x % 2 == 0}

# генерит словарь
a3 = {x: 123 for x in a if x % 2 == 0}

# генерит генератор, не кортеж
# то же самое, что и функция с yield
a4 = (x for x in a if x % 2 == 0)

print(a1, a2, a3, a4)
"""
Задание: В SuperInt заменить итератор на генератор
удаляем SuperIntIterator
метод __iter__ должна вернуть результат выполнения функции-генератора (в которой написан yield)
Ну и саму эту функцию надо написать

    def __iter__(self):
        return self.my_generator(self).__iter__()
"""