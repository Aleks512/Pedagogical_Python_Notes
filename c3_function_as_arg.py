# Pass the function as an argument to another function 
# third_function and fourth_function are what we call HOF - Higher Order Functions as they take as their arguments, other functions.
from c2_function_as_variable import some_variable, other_variable


'''Reminder : Both Funtctions : text_titles and power were assigned to 
            some_varaiable and other_variable, let's use them here'''


#  Higher order function taking other func as argument
def third_function(func, *args) -> int:
    return func(*args)


def fourth_function(func, text: str) -> str:
    return func(text)

# Other exemple

# First class function

def iterable_production(n: int) -> list[int]:
    numbers = []
    for x in range(1, n+1):
        numbers.append(x)
    return numbers

# Higher order function

def do_sth_with_iterable(func, n) -> list[int]:
    outcome = []
    for x in func(n):
        outcome.append(x**n)
    return outcome

# Exemple of HOF using 2 first class functions

def square(x : int) -> int: # First class function
    return x*x

def do_sthElse_with_iterable(func) -> int: #  HOF
    results = []
    my_iterable = iterable_production(10) # calling 2nd First class function
    for i in my_iterable:
        results.append(func(i)) # # First class function as arg
    return results

if __name__ == "__main__":
    # using imported variable/function as arg
    int_result = third_function(other_variable, 2, 3)
    print(int_result)  # 8

    # using imported variable/function as arg
    str_result = fourth_function(some_variable, "dear siR or MADAME, life is BEAUTIFUL, enjoy !")
    print(str_result)  # Dear Sir Or Madame, Life Is Beautiful, Enjoy !
    
    print(do_sth_with_iterable(iterable_production, 10)) # [1, 1024, 59049, 1048576, 9765625, 60466176, 282475249, 1073741824, 3486784401, 10000000000]
    print(do_sthElse_with_iterable(square))  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
