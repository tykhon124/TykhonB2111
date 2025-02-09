class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")


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
            f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Total: {self.calculate_total_price()}")


if __name__ == "__main__":
    # Тестування класів
    account = BankAccount("123456", 1000)
    account.deposit(500)
    account.withdraw(300)
    account.withdraw(1500)

    car = Car("Toyota", "Camry", 2020)
    print(car.get_info())

    employee = Employee("Іван", "Менеджер", 50000)
    print(employee.get_salary_info())

    rectangle = Rectangle(5, 10)
    print("Area:", rectangle.calculate_area())
    print("Perimeter:", rectangle.calculate_perimeter())

    product = Product("Laptop", 1000, 3)
    product.display_info()