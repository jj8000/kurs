"""
Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu
pracy oraz wypłacanie pensji na podstawie zadanej stawki
godzinowej. Jeżeli pracownik będzie pracował więcej niż 8 godzin
(podczas pojedynczej rejestracji czasu) to kolejne godziny policz
jako nadgodziny (z podwójną stawką godzinową).
# Przykład użycia:
# >>> employee = Employee('Jan', 'Nowak', 100.0)
# # >>> employee.register_time(5)
# >>> employee.pay_salary()
# 500.0
# >>> employee.pay_salary()
# 0.0
# >>> employee.register_time(10)
# >>> employee.pay_salary()
# 1200.0


# >>> b = Biuro()
# >>> b.add_employee(employee)
# >>> b.export('dane.csv')
"""

import csv

class Employee:
    def __init__(self, name, surname, rate):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.time = 0

    def register_time(self, time = int):
        self.time += time


    def pay_salary(self):
        if self.time <= 8:
            to_pay = self.time * self.rate
            self.time = 0
            return to_pay
        else:
            to_pay = 8 * self.rate + (self.time - 8) * 2 * self.rate
            self.time = 0
            return to_pay


class Biuro:
    def __init__(self):
        self.employees = []
rkljklrgkjlgr
    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def export(self, filename: str):
        with open(filename, 'w') as k:
            writer = csv.writer(k, delimiter=";")
            writer.writerow(["name", "surname", "rate", "hours"])
            writer.writerows



