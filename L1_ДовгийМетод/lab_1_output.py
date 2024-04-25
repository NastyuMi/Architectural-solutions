class Employee:
    def calculate_salary(self):
        raise NotImplementedError

class HourlyEmployee(Employee):
    def __init__(self, hours, hourly_rate):
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours * self.hourly_rate

class SalariedEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary

def calculate_total_salary(employees):
    total_salary = 0
    for employee in employees:
        total_salary += employee.calculate_salary()

    return total_salary
