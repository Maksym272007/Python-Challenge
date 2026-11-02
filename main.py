def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Bye, {name}!"

try:
    input_name = input("Enter name: ")

    if not input_name.strip():
        raise ValueError("You write nothing!")
except ValueError as error:
    print(f"Error: {error}")
else:
    print(greet(input_name))
    print(farewell(input_name))