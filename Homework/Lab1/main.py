def SquaresBefore(x: int):
    answer = {}
    if (x > 100) or (x < 1):
        print("Вы должны ввести натуральное число не больше 100")
    else:
        for i in range(x+1):
            answer.update({i: [i**2, i**3]})
        return answer

def SquaresBetween(a: int, b: int):
    answer = []
    if (a > b) or (abs(a or b) > 100):
        print("Вы должны ввести число по модулю не больше 100, второе число должно быть больше или равно первому")
    else:
        for i in range(a, b+1):
            answer.append(i**2)
        return answer

def SumOfSquaresBetween(a: int, b: int):
    answer = 0
    if (a > b) or (abs(a or b) > 100):
        print("Вы должны ввести число по модулю не больше 100, второе число должно быть больше или равно первому")
    else:
        for i in range(a, b+1):
            answer += i**2
        return answer

def IsNumbersAscending(x: int):
    x = str(x)
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            return False
    return True

if __name__ == '__main__':
    print("Квадраты и кубы чисел вплоть до введённого числа.")
    input_x = int(input("Введите натуральное число до 100:"))
    print(SquaresBefore(input_x))
    print("Квадраты чисел вплоть от первого введённого числа до второго введённого числа.")
    input_x, input_y = map(int, input("Введите натуральные числа по модулю не больше 100:").split())
    print(SquaresBetween(input_x, input_y))
    print("Сумма квадратов чисел вплоть от первого введённого числа до второго введённого числа.")
    input_x, input_y = map(int, input("Введите натуральные числа по модулю не больше 100:").split())
    print(SumOfSquaresBetween(input_x, input_y))
    print("Проверка находятся ли цифры во введённом числе в порядке возрастания.")
    input_x = int(input("Введите целое число:"))
    print(IsNumbersAscending(input_x))


