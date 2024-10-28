number = 100

Input = int(input("What is my number? "))
print(f"You have chosen {Input}")
if Input == number:
    print(f"You are correct! The number is {number}")
elif Input > number:
    print("You are too high")
elif Input < number:
    print("You are to low")