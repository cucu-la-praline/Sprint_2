class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours  = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        email =  f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
       return self.hours * self.hourly_payment
    

# Примеры использования:
# Создаем сотрудника с известными часами
emp1 = EmployeeSalary("Иван", 40, 2, "ivan@example.com")
print(f"Зарплата Ивана: {emp1.salary()}")  # 40 * 400 = 16000

# Создаем сотрудника, часы которого нужно рассчитать
emp2 = EmployeeSalary.get_hours("Мария", 2, "maria@example.com")
print(f"Часы Марии: {emp2.hours}")  # (7-2)*8 = 40
print(f"Зарплата Марии: {emp2.salary()}")  # 40 * 400 = 16000

# Создаем сотрудника, email которого нужно сгенерировать
emp3 = EmployeeSalary.get_email("Петр", 35, 2)
print(f"Email Петра: {emp3.email}")  # petr@email.com

# Меняем почасовую оплату для всех
EmployeeSalary.set_hourly_payment(450)
print(f"Новая зарплата Ивана: {emp1.salary()}")  # 40 * 450 = 18000
print(f"Новая зарплата Марии: {emp2.salary()}")  # 40 * 450 = 18000