# FullTimeEmployee    c
#include name id     monthly_salary    daily_salary
class Employee:
    def __init__(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id

    def print_info(self):
        print(f"name :{self.name},id:{self.employee_id}")

class FullTimeEmployee(Employee):
    def __init__(self,name,employee_id,monthly_salary):
        super().__init__(name,employee_id)
        self.monthly_salary=monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self,name,employee_id,daily_salary,work_days):
        super().__init__(name, employee_id)
        self.daily_salary = daily_salary
        self.work_days=work_days
    def calculate_daily_pay(self):
        return self.daily_salary * self.work_days

zhang=FullTimeEmployee("张三",10086,6000)
li =PartTimeEmployee("李四",10011,150,15)
li.print_info()
print(li.calculate_daily_pay())
zhang.print_info()
print(zhang.calculate_monthly_pay())
