from dateutil.parser import parse  # надо установить


class DateDict(dict):
    def __setitem__(self, key, value):
        # TODO: Проверить что key это строка (и желательно что строка с датой)
        # FIXME: Заметка чтобы что-то исправить
        key_date = parse(key).date()

        # дополнили родительский setitem
        super().__setitem__(key_date, value)  # вызываю родительский setitem

    def __getitem__(self, key):
        key_date = parse(key).date()
        return super().__getitem__(key_date)


d = DateDict()

d['25.03.2021'] = 354
d['25/03/2021'] = 358  # перезаписать предыдущую строку
d['26 mar 2021'] = 548
d['2021-03-27'] = 456

print(d)
print(d['2021-03-26']) # 548, хотя при создании ключ был в другом формате
