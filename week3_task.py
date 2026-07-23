# class student:
#     def display(self):
#         print("hello i am a student")
# s1=student()
# s1.display()

# class book:
#     def display(self):
#         print("Aurthor name is :shajahan")
# s1=book()
# s1.display()

# class dog:
#     def display(self):
#         print(" The dog is barking")
# s1=dog()
# s1.display()

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# s1 = Student("sahinali", 19)
# print("Name:", s1.name)
# print("Age:", s1.age)

# class car:
#     def __init__(self, brand, colour):
#         self.brand = brand
#         self.colour = colour
# s1 = car("BMW","black")
# print("brand:",s1.brand)
# print("colour:",s1.colour)

# class bank_account:
#     def __init__(self, account, balance):
#         self.account = account
#         self.balance = balance
# s1 = bank_account(115010000154,500.54)
# print("account:",s1.account)
# print("balance:",s1.balance)
# class student:
#     def __init__(self, name, rollno, marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#         print("name:",self.name)
#         print("mark:",self.marks)
#         if self.marks >= 50:
#             print("Result: Pass")
#         else:
#             print("Result: Fail")
# s1 = student("Sahin", 101, 75)
# s2 = student("shajhan", 102, 45)

# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary
#         print("name:",self.name)
#         print("employee_id;",self.emp_id)
#         print("salary:",self.salary)
#         if self.salary >= 10000:
#             bonus = self.salary * 0.10
#             print("Bonus:", bonus)
#         else:
#             bonus = self.salary * 0.05
#             print("Bonus:", bonus)
# e1 = Employee("saihin", 101, 12000)
# e2 = Employee("shajahan", 102, 80000)
# e3 = Employee("akthas", 103, 13000)
# e4 = Employee("jishan", 104, 9500)

# class Laptop:
#     def __init__(self, brand, ram):
#         self.brand = brand
#         self.ram = ram
#     def display(self):
#         print("Brand:", self.brand)
#         print("RAM:", self.ram)
# l1 = Laptop("Dell", "8 GB")
# l2 = Laptop("HP", "16 GB")
# print("Laptop 1")
# l1.display()
# print("laptop 2")
# l2.display()

# class Movie:
#     def __init__(self, movie_name, director_name, rating):
#         self.movie_name = movie_name
#         self.director_name = director_name
#         self.rating = rating
#     def display(self):
#         print("Movie Name:", self.movie_name)
#         print("Director Name:", self.director_name)
#         print("Rating:", self.rating)
# movie_name = input("Enter the movie name: ")
# director_name = input("Enter the director name: ")
# rating = float(input("Enter the rating: "))
# m1 = Movie(movie_name, director_name, rating)
# print("Movie ")
# m1.display()

# class MovieTicket:
#     def __init__(self, ticket_id, customer_name, movie_name, seats):
#         self.ticket_id = ticket_id
#         self.customer_name = customer_name
#         self.movie_name = movie_name
#         self.seats = seats
#     def display(self):
#         print("\nTicket ID:", self.ticket_id)
#         print("Customer Name:", self.customer_name)
#         print("Movie Name:", self.movie_name)
#         print("Number of Seats:", self.seats)
# n = int(input("How many movie tickets do you want to book? "))
# tickets = []
# for i in range(n):
#     print("\nEnter details for Ticket", i + 1)
#     ticket_id = int(input("Enter Ticket ID: "))
#     customer_name = input("Enter Customer Name: ")
#     movie_name = input("Enter Movie Name: ")
#     seats = int(input("Enter Number of Seats: "))
#     ticket = MovieTicket(ticket_id, customer_name, movie_name, seats)
#     tickets.append(ticket)
# print("\nMovie Ticket Details")
# for ticket in tickets:
#     ticket.display()

# class Animal:
#     def eat(self):
#         print("Animal is eating")
# class Cat(Animal):
#     def sleep(self):
#         print("Cat is sleeping")
# s1 = Cat()
# s1.eat()
# s1.sleep()

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
# s1 = person("sahinali",19)
# s1.display()
# class student(person):
#     def __init__(self, course, rollno):
#         self.course = course
#         self.rollno = rollno
#     def display(self):
#         print("Course:",self.course)
#         print("rollno:",self.rollno)
# s1 = student("b.tech",4106)
# s1.display()

# class vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def display(self):
#         print("brand:",self.brand)
#         print("model:",self.model)
# s1 = vehicle("bmw",2021)
# s1.display()
# class car(vehicle):
#     def __init__(self, seating, fueltype):
#         self.seating = seating
#         self.fueltype = fueltype
#     def display(self):
#         print("seating:",self.seating)
#         print("fueltype:",self.fueltype)
# s1 = car("4 seater", "disel")
# s1.display()


# class bank_acc:
#     def __init__(self, acc_no, name):
#         self.acc_no = acc_no
#         self.name = name

#     def display_acc(self):
#         print("Account Number:", self.acc_no)
#         print("Account Holder:", self.name)

# class savings(bank_acc):
#     def __init__(self, acc_no, name, balance):
#         super().__init__(acc_no, name)
#         self.balance = balance

#     def display_balance(self):
#         print("Current Balance:", self.balance)
           
# class online_banking(savings):
#     def check_balance(self):
#         print("Available Balance:", self.balance)
# acc1 = online_banking(12345, "Pooja", 5000)
# acc1.display_acc()
# acc1.display_balance()
# acc1.check_balance()

# class Customer:
#     def __init__(self, name, mobile_no):
#         self.name = name
#         self.mobile_no = mobile_no
#     def display(self):
#         print("Customer Name:", self.name)
#         print("Mobile No:", self.mobile_no)

# class Order(Customer):
#     def __init__(self, name, mobile_no, product_name, quantity, price):
#         super().__init__(name, mobile_no)
#         self.product_name = product_name
#         self.quantity = quantity
#         self.price = price
#     def total(self):
#         return self.quantity * self.price
#     def display_order(self):
#         print("\nProduct:", self.product_name)
#         print("Quantity:", self.quantity)
#         print("Price:", self.price)
#         print("Total:", self.total())
# class Payment(Order):
#     def make_payment(self):
#         total_amount = self.total()
#         if total_amount >= 0:
#             print("Payment Successful")
#             print("Paid Amount:", total_amount)
#         else:
#             print("Invalid Order")

# name = input("Enter customer name: ")
# mobile = input("Enter mobile number: ")
# product = input("Enter product name: ")
# qty = int(input("Enter quantity: "))
# ,mprice = float(input("Enter price: "))

# obj = Payment(name, mobile, product, qty, price)

# obj.display()
# obj.display_order()
# obj.make_payment()

# class Login:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def login(self):
#         if self.username == "shajahan" and self.password == "123456":
#             print("Login successful ")
#             return True
#         else:
#             print("Login failed ")
#             return False
# class FoodOrder:
#     def __init__(self):
#         self.menu = {"burger": 369, "pizza": 299,"leg65":199,"kaluth kari":10}

#     def show_menu(self):
#         print("\n--- Menu ---")
#         for item, price in self.menu.items():
#             print(item, "=", price)

#     def order(self):
#         while True:
#             self.show_menu()

#     item = input("Enter food item: ").lower()

#     if item in self.menu:
#         qty = int(input("Enter quantity: "))
#         total = self.menu[item] * qty
#         print("Item:", item)
#         print("Quantity:", qty)
#         print("Total bill:", total)
#         print("Order placed successfully ")
#     else:
#         print("Food item not available ")
# a = Login("shajahan", "123456")

# if a.login():
#     f = FoodOrder()
#     f.order()

        
class User:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
    def display_user(self):
        print("Name:", self.name)
        print("Email:", self.mail)

class Student(User):
    def __init__(self, name, mail, course):
        super().__init__(name, mail)
        self.course = course
    def display_student(self):
        self.display_user()
        print("Course:", self.course)

class Instructor(User):
    def __init__(self, name, mail, course):
        super().__init__(name, mail)
        self.course = course
    def display_instructor(self):
        self.display_user()
        print("Course:", self.course)

name = input("Enter student name: ")
mail = input("Enter student email: ")
course = input("Enter student course: ")
s = Student(name, mail, course)

iname = input("\nEnter instructor name: ")
imail = input("Enter instructor email: ")
icourse = input("Enter instructor course: ")
i = Instructor(iname, imail, icourse)

print("\nStudent Details")
s.display_student()
print("\nInstructor Details")
i.display_instructor()

