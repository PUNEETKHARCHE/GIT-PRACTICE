def empty_function():
    pass


# function definition
# - declaration (signature) + body
# - parameterless function
def function1():
    print("inside function1")


# function call or invocation
# function1()


# parameterized
# - all parameters are by default mandatory
def function2(p1: int, p2: int):
    result = p1 + p2
    print(f"result = {result}")


# indexed parameters
# function2(10, 20)

# named parameters
# function2(p1=10, p2=20)
# function2(p2=20, p1=10)

# mixed
# function2(10, p2=20)


# parameterized function
# - p1 and p2 are mandatory
# - p3 is optional parameter as it has got a default value
def function3(p1: int, p2: int, p3=10):
    print(f"p1 = {p1}, p2 = {p2}, p3 = {p3}")


# function3(100, 200, 300)
# function3(100, 200)
# function3(p1=100, p2=200)
