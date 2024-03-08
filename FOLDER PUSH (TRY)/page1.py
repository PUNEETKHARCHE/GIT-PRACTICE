# for..in loop

def function1():
    number = 9
    is_prime = True
    for index in range(2, number):
        if number % index == 0:
            is_prime = False
            break

    if is_prime:
        print("this is a prime number")
    else:
        print(f"number is not prime")


# function1()


def function2():
    for index in range(5):
        if index > 3:
            break
        print(f"index = {index}")
    else:
        # this block will be called only when the for loop
        # gets exhausted (completed)
        print("else block is called")


# function2()


def function3():
    number = 10
    for index in range(2, number):
        if number % index == 0:
            print("this is not a prime number")
            break
    # this else block is associated with for loop
    # and not the if condition
    else:
        # this block will be called only when the for
        # loop completed all iterations
        print("this number is a prime number")

    print("this is last line of function3")


function3()

