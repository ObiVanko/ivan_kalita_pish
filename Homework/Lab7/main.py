from functools import reduce

# Задание 1: Возведение чисел в квадрат
numbers_1 = [1, 2, 3, 4, 5]
answer_1 = list(map(lambda x: x**2, numbers_1))
print(answer_1)

# Задание 2: Фильтрация чётных чисел
numbers_2 = [10, 15, 20, 25, 30]
answer_2 = list(filter(lambda x: x % 2 == 0, numbers_2))
print(answer_2)

# Задание 3: Сортировка списка слов по длине
words_3 = ["apple", "banana", "pear", "grape", "kiwi"]
answer_3 = list(sorted(words_3, key=lambda x: len(x)))
print(answer_3)

# Задание 4: Произведение всех чисел в списке
numbers_4 = [1, 2, 3, 4]
answer_4 = reduce(lambda x, y: x * y, numbers_4)
print(answer_4)

# Задание 5: Проверка на палиндромы
words_5 = ["level", "world", "radar", "python", "madam"]
answer_5 = list(filter(lambda x: x[:len(x)//2:] == ((x[len(x) - (len(x)//2)::])[::-1]), words_5))
print(answer_5)