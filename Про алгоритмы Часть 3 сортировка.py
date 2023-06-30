a = [19, 22, 16, 44, 21, 34, 55, 12, 45]

# Сложность: сравнений O(n**2)
# Количество перестановок O(n)
def selection_sort(iterable):
    for left in range(0, len(iterable) - 1):
        minimum = iterable[left]
        minimum_idx = left
        for i in range(left, len(iterable)):
            if iterable[i] < minimum:
                minimum = iterable[i]
                minimum_idx = i

        print(left, minimum, iterable)

        # Классическая перестановка
        tmp = iterable[left]
        iterable[left] = iterable[minimum_idx]
        iterable[minimum_idx] = tmp

        # Либо переставить так
        # Через создание и распаковку кортежа
        # iterable[left], iterable[minimum_idx] = iterable[minimum_idx], iterable[left]

selection_sort(a)
