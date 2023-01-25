# Simple functions

def power(a: int, b: int) -> int:
    ''' power : Returns first "a" integer raised to power second "b" integer'''
    return a**b


def make_title(text: str) -> str:
    ''' make_title : Returns string representation as title'''
    return text.title()


if __name__ == "__main__":
    number = power(6, 3)  
    text = make_title("THE BEST FILM EVER")

    print(number)  # 216
    print(text)  # The Best Film Ever 