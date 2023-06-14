print('задание: 1')
class Salary:
    def __init__(self, rate, days_worked):
        self.rate = rate
        self.days_worked = days_worked
    
    def calculate_salary(self, sale_volume=0):
        base_salary = self.rate * self.days_worked
        if sale_volume > 0:
            bonus = sale_volume * 0.1
            total_salary = base_salary + bonus
            return total_salary
        else:
            return base_salary

salary = Salary(100, 22)
print("Salary without bonus:", salary.calculate_salary())
print("Salary with bonus:", salary.calculate_salary(5000))
print('')

print('задание: 2')
class Salary:
    def __init__(self, rate, days_worked):
        self.rate = rate
        self.days_worked = days_worked
    
    def calculate_salary(self, sale_volume=0):
        base_salary = self.rate * self.days_worked
        if sale_volume > 1000000:
            bonus = sale_volume * 0.1
            total_salary = base_salary + bonus
            return total_salary
        else:
            penalty = sale_volume * 0.1
            total_salary = base_salary - penalty
            return total_salary

salary = Salary(100, 22)
print("Salary without bonus or penalty:", salary.calculate_salary())
print("Salary with bonus:", salary.calculate_salary(1500000))
print("Salary with penalty:", salary.calculate_salary(5000))
print('')

print('Задание: 3')
class Employee:
    def __init__(self, rate, days_worked):
        self.rate = rate
        self.days_worked = days_worked
    
    def calculate_salary(self, sale_volume=0):
        pass

class SalesEmployee(Employee):
    def calculate_salary(self, sale_volume=0):
        base_salary = self.rate * self.days_worked
        if sale_volume > 0:
            bonus = sale_volume * 0.1
            total_salary = base_salary + bonus
            return total_salary
        else:
            return base_salary

class WarehouseEmployee(Employee):
    def calculate_salary(self, sale_volume=0):
        if self.days_worked > 20:
            base_salary = self.rate * self.days_worked
            return base_salary
        else:
            return 0

sales_employee = SalesEmployee(100, 22)
print("Sales Employee Salary:", sales_employee.calculate_salary(5000))

warehouse_employee = WarehouseEmployee(80, 15)
print("Warehouse Employee Salary:", warehouse_employee.calculate_salary())
print('')

print('Задание: 4')
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, rate, days_worked):
        self.rate = rate
        self.days_worked = days_worked
    
    @abstractmethod
    def calculate_salary(self, sale_volume=0):
        pass

class SalesEmployee(Employee):
    def calculate_salary(self, sale_volume=0):
        base_salary = self.rate * self.days_worked
        if sale_volume > 0:
            bonus = sale_volume * 0.1
            total_salary = base_salary + bonus
            return total_salary
        else:
            return base_salary

class WarehouseEmployee(Employee):
    def calculate_salary(self, sale_volume=0):
        if self.days_worked > 20:
            base_salary = self.rate * self.days_worked
            return base_salary
        else:
            return 0

sales_employee = SalesEmployee(100, 22)
print("Sales Employee Salary:", sales_employee.calculate_salary(5000))

warehouse_employee = WarehouseEmployee(80, 15)
print("Warehouse Employee Salary:", warehouse_employee.calculate_salary())
print('')    

print('Задание: 5')
class Furniture:
    def __init__(self, material, color, price):
        self.material = material
        self.color = color
        self.price = price
        
    def description(self):
        print("This piece of furniture is made of", self.material, "and is", self.color, "in color. It costs", self.price, "rubls.")

class Cabinet(Furniture):
    def __init__(self, material, color, price, num_drawers):
        super().__init__(material, color, price)
        self.num_drawers = num_drawers
        
    def description(self):
        super().description()
        print("This cabinet has", self.num_drawers, "drawers.")
        
class Sofa(Furniture):
    def __init__(self, material, color, price, num_seats):
        super().__init__(material, color, price)
        self.num_seats = num_seats
        
    def description(self):
        super().description()
        print("This sofa has", self.num_seats, "seats.")
        
class DiningTable(Furniture):
    def __init__(self, material, color, price, shape):
        super().__init__(material, color, price)
        self.shape = shape
        
    def description(self):
        super().description()
        print("This dining table is", self.shape, "in shape.")

cabinet = Cabinet("wood", "brown", 7000, 3)
sofa = Sofa("leather", "black", 000, 2)
dining_table = DiningTable("glass", "clear", 8500, "rectangle")

cabinet.description()
sofa.description()
dining_table.description()