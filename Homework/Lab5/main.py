
# Задание 1: Парсинг CSV
data_1 = "Иванов Иван, 20, Математика; Петров Петр, 21, Физика; Сидоров Сидор, 22, Химия"

students = data_1.split(";")
for i in students:
    info = i.split(",")
    print("Имя: " + info[0].strip())
    print("Возраст: " + info[1].strip())
    print("Факультет: " + info[2].strip() + "\n")

# Задание 2: Извлечение email-адресов
text_2 = "Контакты: ivanov@example.com, petrov@work.net, sid@mail.ru"

answer_2 = list(map(lambda x: x.strip(), text_2.replace("Контакты:", "").split(",")))
print(f"Список адресов: {answer_2}")

# Задание 3: Подсчет количества слов
sentence_3 = "Python is a powerful and easy-to-learn programming language."
answer_3 = len(sentence_3.split())
print(f"Количество слов: {answer_3}")

# Задание 4: Удаление дубликатов символов
s_4 = "aaabbbcccaaadddd"
answer_4 = ""
for i in range(len(s_4)-1):
    if s_4[i] != s_4[i+1]:
        answer_4 += s_4[i]
answer_4 += s_4[-1]

print(f"Очищенная строка: {answer_4}")

# Задание 5: Извлечение чисел
text_5 = "Сегодня 20 градусов, завтра будет 18 градусов, а вчера было 22 градуса."
answer_5 = list(filter(lambda x: x.isdigit(), text_5.split()))

print(f"Числа в строке: {answer_5}")