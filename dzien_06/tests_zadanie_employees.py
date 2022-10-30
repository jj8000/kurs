from zadanie_employees import Employee, Biuro

def test_Employee_init():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee
    assert employee.rate == 100.0


def test_Employee_pay_salary():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.pay_salary() == 0


def test_Employee_register_time():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.time == 0
    employee.register_time(5)
    assert employee.time == 5


def test_Employee_pay_salary_after_register_time():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500
    assert employee.pay_salary() == 0


def test_Employee_pay_salary_over_time_hours():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    assert employee.pay_salary() == 1200
    assert employee.pay_salary() == 0

def test_Biuro():
    assert Biuro()

def test_Biuro_add_employee():
    b = Biuro()
    employee = Employee('Jan', 'Nowak', 100.0)
    b.add_employee(employee)
