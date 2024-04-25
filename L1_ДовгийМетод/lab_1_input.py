def calculate_total_salary(employees):
    total_salary = 0
    for employee in employees:
        if employee.is_hourly:
            total_salary += employee.hours * employee.hourly_rate
        else:
            total_salary += employee.salary

    return total_salary
