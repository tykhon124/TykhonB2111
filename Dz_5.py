from colorama import init, Fore, Back, Style


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(Fore.GREEN + f"Deposited {amount}. New balance: {self.balance}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Deposit amount must be positive." + Style.RESET_ALL)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(Fore.YELLOW + f"Withdrawn {amount}. New balance: {self.balance}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Insufficient funds or invalid amount." + Style.RESET_ALL)


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary}"


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        print(
            Fore.CYAN + f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Total: {self.calculate_total_price()}" + Style.RESET_ALL)


if __name__ == "__main__":
    init()

    # Тестування класів
    account = BankAccount("123456", 1000)
    account.deposit(500)
    account.withdraw(300)
    account.withdraw(1500)

    car = Car("Toyota", "Camry", 2020)
    print(Fore.BLUE + car.get_info() + Style.RESET_ALL)

    employee = Employee("Іван", "Менеджер", 50000)
    print(Fore.MAGENTA + employee.get_salary_info() + Style.RESET_ALL)

    rectangle = Rectangle(5, 10)
    print(Fore.YELLOW + "Area:" + Style.RESET_ALL, rectangle.calculate_area())
    print(Fore.YELLOW + "Perimeter:" + Style.RESET_ALL, rectangle.calculate_perimeter())

    product = Product("Laptop", 1000, 3)
    product.display_info()
