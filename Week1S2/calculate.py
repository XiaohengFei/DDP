def add(num1,num2):
    return (num1+num2)

def add_one(num1):
    return num1 + 1

def minus (num1,num2):
    return num1 - num2

def multiplication (num1,num2):
    return  num1 * num2

def divided_by (num1,num2):
    return num1 / num2

print(add(2,3))

def calculater():
    print("Select type of operation:")
    print("1, Add")
    print("2, Substract")
    print("3, Multiply")
    print("4, Dived")

    choice = int(input("Enter number"))
    num1 = int(input("first num"))
    num1 = int(input("Enter number: "))
    num2 = int(input("second num"))
    if choice == "1":
        print (add(num1, num2))
    elif choice == "2":
        print (minus(num1, num2))
    elif choice == "3":
        print (multiplication(num1, num2))
    elif choice == "4":
        print (divided_by(num1, num2))

calculater()