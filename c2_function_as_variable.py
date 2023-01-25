# Assign function to variable
from concept_1 import make_title, power

some_variable = make_title
other_variable = power


result_title = some_variable("cats are the best ")
result_power = other_variable(3, 4)

if __name__ == "__main__":
    print(result_title)  # Cats Are The Best
    print(result_power) #  81
