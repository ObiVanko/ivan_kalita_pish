
def f(x):
    if x >= 2:
        return (x**2 + 4*x + 5)
    elif x < -2:
        return 4
    else:
        return x**2

def nod(a, b):
    while (a != 0 and b != 0):
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

def amount_digits(x: int):
    answer = 0
    while x > 0:
        answer += x % 10
        x = x // 10
    return answer

def product_digits(x: int):
    answer = 1
    while x > 0:
        answer *= x % 10
        x = x // 10
    return answer

def amount_equal_product_digits(x: int):
    if amount_digits(x) == product_digits(x):
        return True
    else:
        return False

if __name__ == '__main__':
    print("Функция F(x).")
    input_x = int(input("Введите число х: "))
    print(f(input_x))
    print("Поиск наибольшего общего делителя.")
    input_x, input_y = map(int, input("Введите числа для поиска общего делителя: ").split())
    print(nod(input_x, input_y))
    print("Сумма цифр введённого числа.")
    input_x = int(input("Введите число: "))
    print(amount_digits(input_x))
    print("Проверка равна ли сумма цифр числа их произведению.")
    input_x = int(input("Введите число: "))
    print(amount_equal_product_digits(input_x))
