# Pass the function as an argument to another function 

from c2_function_as_variable import some_variable, other_variable


'''Reminder : Both Funtctions : text_titles and power were assigned to 
            some_varaiable and other_variable, let's use them here'''


def third_function(func, *args) -> int:
    '''Third function will return the power based on only 2 arg'''
    return func(*args)


def fourth_function(func, text: str) -> str:
    '''This function'''
    return func(text)


if __name__ == "__main__":
    # using variable/function as arg
    int_result = third_function(other_variable, 2, 3)
    print(int_result)  # 8
    # using variable/function as arg
    str_result = fourth_function(some_variable, "dear siR or MADAME, life is BEAUTIFUL, enjoy !")
    print(str_result)  # Dear Sir Or Madame, Life Is Beautiful, Enjoy !