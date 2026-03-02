first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

try:
    age = int(input("Enter age: "))
    
    if age < 0:
        print("Age cannot be negative")
    else:
        print("Full Name:", first_name + " " + last_name)
        print("You will be", age + 1, "next year")

except ValueError:
    print("Invalid age input")