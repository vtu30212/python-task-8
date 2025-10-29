def get_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0:
                raise ValueError("Age cannot be negative.")
            return age
        except ValueError as ve:
            print("Invalid input:", ve)

try:
    age = get_age()
    print("Your age is:", age)
except ValueError as ve:
    print("An error occurred:", ve)
