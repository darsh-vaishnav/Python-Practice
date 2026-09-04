# cw 
name=input("Enter your name: ")
age=int(input("Enter your age: "))
lab=input("Enter your lab: ")
Product_name=input("Enter your Product name: ")
Product_price=float(input("Enter your Product price: "))
Product_quantity=int(input("Enter your Product quantity: "))
Product_total=(Product_quantity)*(Product_price)

print(f"Name {name}")
print(f"Age {age}")
print(f"Lab {lab}")
print(f"Product Name {Product_name}")
print(f"Product Price {Product_price}")
print(f"Product Quantity {Product_quantity}")
print(f"Product Total {Product_total}")

print(type(name))
print(type(age))
print(type(lab))
print(type(Product_name))
print(type(Product_price))
print(type(Product_quantity))
print(type(Product_total))

#Que 1
name=input("Enter your name: ")
print(f"Your name is {name}")

#Que 2
city=input("Enter your city: ")
print(f"Your city is {city}")

#Que 3
user_name=input("Enter your Name:")
age=int(input("Enter your Age:"))
print(f"User name is {user_name} and your age is {age}")

#Que 4
#input()generally returns a string (str) by default

#Que 5
name=input("Enter your name: ")
age=int(input("Enter your age: "))
lab=input("Enter your lab: ")

print(f"Name {name}")
print(f"Age {age}")
print(f"Lab {lab}")

print(type(name))
print(type(age))
print(type(lab))

#Que 6
first_name=(input("Enter your first_name:"))
last_name=(input("Enter your last_name:"))

print(first_name+" "+last_name)

#Que 7
name=input("Enter your name: ")
city=input("Enter your city: ")
collage=input("Enter your collage: ")

print(f"Name {name}")
print(f"City {city}")
print(f"Collage {collage}")

#Que 8
name1,name2=input("Enter two names: ").split()

print("Name 1:",name1)
print("Name 2:",name2)

#Que 9
first_name,last_name=input("Enter first name and last name: ").split()
print(first_name)
print(last_name)

#Que 10
first_name,middle_name,last_name=input("Enter first name, middle name, and last name: ").split()
print(first_name)
print(middle_name)
print(last_name)

#Que 11
number=int(input("Enter a number: "))
print(f"The number is {number}")
# #Input: "25" → str
# #Conversion: int("25")
# #Output: 25 → int

#Que 12
number=float(input("Enter a number: "))
print(f"The number is {number}")
# #Input: "25.5" → str
# #Conversion: float("25.5")
# #Output: 25.5 → float

#Que 13
number=int(input("Enter a number: "))
variable=str(number)
print(f"The number is {variable}")

#Que 14
number=int(input("Enter a number: "))
print(f"The number is {number}")
print(type(number))

#Que 15
number=float(input("Enter a number: "))
print(f"The number is {number}")
print(type(number))

#Que 16
a=input("Enter number a: ")
b=input("Enter number b: ")

print(a + b)
#Because input() returns values as strings, so + performs string concatenation instead of numeric addition.

#Que 17
# this is our old program it will create the answer in the string form whereas we want ans in the integer form so then we can use to rapping the input() function
# # a = input("Enter first number: ")
# # b = input("Enter second number: ")

# print(a + b)
a = input("Enter first number: ")
b = input("Enter second number: ")

print(int(a) + int(b))
#-----------------------------------------------------------------------------------------------------------------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)

#Que 18
name=input("Enter your name: ")
age=int(input("Enter your age: "))

print(f"My Name is {name} and I am {age} years old.")

#Que 19
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"The sum of {a} and {b} is {a+b}.")

#Que 20
user_name=input("Enter your User_name: ")
age=int(input("Enter your age: "))

print(f"My Name is {user_name} and I am {age} years old.")

#Que 21
product_price=float(input("Enter the Product price: "))
print(f"The Product price is {product_price:.2f}")

#Que 22
#In an f-string, :.2f formats a number as a floating-point value with exactly 2 digits after the decimal point.

#Que 23
product_name=input("Enter the Product name:")
price=float(input("Enter the product price: "))
quantity=int(input("Enter the product quantity:"))
print(f"Product: {product_name}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")

#Que 24
year=int(input("Enter Year:"))
month=int(input("Enter Month:"))
day=int(input("Enter Day:"))
print(f"Enter the numbers {A},{B},{C}")

#Que 25
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))
print(x,y,z,sep="-")

#Que 26
first_letter=input("Enter first letter:")
last_letter=input("Enter Last letter:")
print(first_letter , end=" ")
print(last_letter)

#Que 27
first_number=int(input("Enter First number:"))
second_number=int(input("Enter Second number:"))
sum=first_number+second_number
print(f"First number:{first_number}")
print(f"Second number:{second_number}")
print(f"Sum:{sum}")

#Que 28
price=int(input("Enter Price:"))
quantity=int(input("Enter Quantity:"))
total=price*quantity
print(f"Price:{price}")
print(f"Quantity:{quantity}")
print(f"Total:{total}")

#Que 29
name=input("Enter Students Name:")
age=float(input("Enter Students Age:"))
marks=float(input("Enter Students Marks:"))
print(f"The Student of class 10 whose is Name {name} was {age} year older has {marks} in the maths")


#Que 30
name=input("Enter Students Name:")
age=int(input("Enter Students Age:"))
height=float(input("Enter Students Height:"))
city=input("Enter Students city:")
print(f"A Student of class 10 whose name is {name} was {age} years older and his height is {height:.2f} was residing from the {city}.")
