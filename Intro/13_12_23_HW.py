def input_positive_number(value1):
    # Функція для введення позитивного числа.
    while True:
        try:
            number = float(input(value1))
            if number > 0:
                return number
            else:
                print("The number must be positive")
        except ValueError:
            print("Please enter a valid number")

def main():
    # Введення першого позитивного числа
    x = input_positive_number("Enter x = ")

    # Введення другого позитивного числа, яке відрізняється від першого
    while True:
        y = input_positive_number("Enter y = ")
        if y != x:
            break
        else:
            print("The numbers should be different")

    # Обчислення та виведення суми
    print(f"{x} + {y} = {x + y}")


if __name__ == "__main__":
    main()