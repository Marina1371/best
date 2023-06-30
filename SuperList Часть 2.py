# Свой тип ошибки
# Просто наследуем ради другого названия
# внутри можно ничего не писать
# ловим его как try... except LengthMismatchError: ...
# Также можно его поместить внутрь SuperList как вложенный класс
# Тогда ловим как SuperList.LengthMismatchError
class LengthMismatchError(Exception):  # несовпадение длины
    pass


class SuperList(list):
    def arithmetic(self, other, method_name, reverse_method_name):
        # Мы целиком заменили, а не дополнили родительский __mul__
        # поэтому super().__mul__() вызывать не будем

        if isinstance(other, SuperList):  # либо isinstance(other, list)
            # умножаем список на список
            if len(self) != len(other):
                raise LengthMismatchError('Длины списков не совпадают')

            res = SuperList(self)
            for i in range(len(res)):  # либо len(self), либо len(other) - они все одинаковые
                #res[i] = res[i].__gt__(other[i])  # здесь предполагаем, что элементы умеют друг на друга умножаться
                # можно сделать проверку hasattr(res[i], method_name)
                res[i] = getattr(res[i], method_name)(other[i])
                if res[i] is NotImplemented:
                    res[i] = getattr(other[i], reverse_method_name)(self[i])

            return res  # список * список = третий новый список
        else:
            # умножаем список на одиночный элемент
            res = SuperList(self)  # скопируем
            for i in range(len(res)):
                res[i] = getattr(res[i], method_name)(other)
                if res[i] is NotImplemented:
                    res[i] = getattr(other, reverse_method_name)(res[i])
            return res

    def __mul__(self, other):
        return self.arithmetic(other, '__mul__', '__rmul__')

    def __gt__(self, other):
        return self.arithmetic(other, '__gt__', '__lt__')


a = SuperList([19, 22, 16, 44, 21, 34, 55, 12, 45])
b = SuperList([100, 1000, 10, 0.1, 10, 10, 10, 100, 1000])
c = [100, 1000, 10, 0.1, 10, 10, 10, 100, 1000]

#
# print(a[[5, 2, 8]])  # 5й, 2й и 8й элемент  __getitem__
print(a * 10)  # умножит всё на 10  __mul__
print(a * b)
print(a > 20)  # получится маска
# print(a[a > 20])  # передали маску из true/False в getitem