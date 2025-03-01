def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Помилка! Ділення на нуль."


def calculator():
    while True:
        print("Виберіть свій спосіб:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Вихід")

        choice = input("Введіть номер операції! (1/2/3/4/5): ")

        if choice == '5':
            print("Вихід з калькулятора.")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))

            if choice == '1':
                print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Неправильний ввід. Спробуйте ще раз.")


if __name__ == "__main__":
    calculator()
