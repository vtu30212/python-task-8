def operation_decorator(func):
    def wrapper(x, y):
        print("Performing arithmetic operation...")
        result = func(x, y)
        print("Operation completed.")
        return result
    return wrapper

@operation_decorator
def add(x, y):
    return x + y

@operation_decorator
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

result_add = add(5, 3)
print("Result of addition:", result_add)
result_divide = divide(15, 0)
print("Result of division:", result_divide)
