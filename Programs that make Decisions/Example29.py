
yourAge = int(input("Enter your age: "))

if yourAge < 13:
    print("You are a child.")
elif yourAge < 18:
    print("You are a teenager.")
elif yourAge < 65:
    print("You are an adult.")
else:
    print("You are a senior.")