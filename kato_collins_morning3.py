class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine Started")
    
    def stop_engine(self):
        print("Engine stopped")


my_car = Car("Tesla","HOnda", 2023)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()

#Bank Problem
class Bank_Account:
    def __init__(self, Account_No, Balance):
        self.Account_No = Account_No
        self.Balance = Balance

    def deposit(self, Amount):
        self.Balance += Amount
        print("Balance:", self.Balance)

    def withdraw(self, Amount):
        self.Balance -= Amount
        print("Balance:", self.Balance)

    def display_balance(self):
        print(self.Balance)

Kato_Acc = Bank_Account("AB2000847K", 30000)

Kato_Acc.deposit(20000)
Kato_Acc.withdraw(5000)
Kato_Acc.display_balance()

# Excercise Calculate ARea and Perimeter of A traingle


class Triangle:
    def __init__(self, base, height, lside, rside):
        self.base = base
        self.height = height
        self.lside = lside
        self.rside = rside
    
    def area(self):
        Area = 0.5 * self.base * self.height
        print("Area:", Area)
        
    def perimeter(self):
        Perimeter = self.base + self.lside + self.rside
        print("Perimeter:", Perimeter)

Tp = Triangle(12, 8, 7, 6)
Tp.area()
Tp.perimeter()
        
#Claculate and display bonus(15) of employee1 : 150000, emplyee2: 230000      
class Bonus:
    def __init__(self, empsalary, empname):
        self.empsalary = empsalary
        self.empname = empname

    def calc_bonus(self):
        bonus = 0.15 * self.empsalary
        print("Bonus:", bonus)

emp1 = Bonus(200000, "Kato")

emp1.calc_bonus()

# Encapsulation

#Convert temperature in celcius to feraheight

class Temp:
    def __init__(self, tempe):
        self._tempe = tempe

    def __calc_fahrenheit(self):
        Ntemp = (self._tempe * (9/5)) + 32
        print(Ntemp,"F")
    
    def show(self):
        print("Am child object")

temper = Temp(40)
temper._Temp__calc_fahrenheit()
print(temper._tempe)
                             
#EXercise encapsulation with employee information to give an increament

class Employee:
	def __init__(self, EmpName, EmpSalary):
		self._EmpName = EmpName #Protected field EmpName
		self.EmpSalary = EmpSalary
		
	def __increament(self, incre_percentage): #Private Method
		self.EmpSalary = ((incre_percentage/100)*self.EmpSalary) + self.EmpSalary
		print("New Salary:", self.EmpSalary)
		
Emp1 = Employee("Kato", 850000)
#Emp1.__increament(40) This gives an error because the method is private and can't be accessed out of class
Emp1._Employee__increament(40) #Accessing Private method outside class Employee

		
