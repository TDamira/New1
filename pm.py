class PM:
    def __init__(self, name, surname, salary):
        self.name = "Ivan"
        self.surname = "Petrov"
        self.salary = 10000
      
    def calculate_overtime_pay(self, overtime_hours):
        overtime_rate = 2  
        salary_per_hour = self.salary / 176
        overtime_pay = overtime_hours * salary_per_hour * overtime_rate
        return overtime_pay
    
pm_employee = PM("Ivan", "Petrov", 10000)            

overtime_pay = pm_employee.calculate_overtime_pay(1)
print(overtime_pay)



