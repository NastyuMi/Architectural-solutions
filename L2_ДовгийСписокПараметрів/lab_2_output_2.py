from enum import Enum

class UserType(Enum):
    ENGINEER = 1
    MANAGER = 2

class User:
    def __init__(self, name, age, user_type: UserType, phone_number: str):
        self.name = name
        self.age = age
        self.user_type = user_type
        self._phone_code, self._phone = phone_number.split()

    def print_details(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Тип користувача: {self.user_type.name}")
        print(f"Номер телефону: {self.get_phone_number()}")

    def get_phone_number(self):
        return f"+{self._phone_code} {self._phone}"

# Приклад використання
user = User("John", 25, UserType.ENGINEER, "380971234567")
user.print_details()
