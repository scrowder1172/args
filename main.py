"""
These examples came from:
https://medium.com/towards-data-science/python-args-kwargs-and-all-other-ways-to-pass-arguments-to-your-function-bd2acdce72b5
"""


def print_variables(var1, var2):
    """
    Print variable names and values
    :param var1: first variable
    :param var2: second variable
    :return: print statement
    """
    return print(f"{var1=} {var2=}")


def the_func(greeting, thing):
    """
    Function that prints out a greeting to a thing
    :param greeting: greeting message
    :param thing: thing that gets greeted
    :return: printed greeting
    """
    return print(f"{greeting} {thing}")


def multiply(a, b, *args):
    """
    Function multiplies arguments together
        Requires at least two numeric values (a, b) and accepts an unlimited additional number of numeric values
    Error handling needed to prevent bad data from being passed
    :param a: numeric
    :param b: numeric
    :param args: tuple of unlimited number of additional numeric values
    :return: printed multiplied result
    """
    result = a * b
    for arg in args:
        result *= arg
    return print(result)


def introduce(firstname, lastname, **kwargs):
    """
    Generate an introduction with firstname and lastname as well as an unlimited number of additional named parameters
        **kwargs is parsed as a dictionary object
    :param firstname: first name
    :param lastname: last name
    :param kwargs: dictionary of unlimited named parameters
    :return: printed introduction statement
    """
    introduction = f"I am {firstname.capitalize()} {lastname.capitalize()}"
    for key, value in kwargs.items():
        introduction += f" my {key} is {value}"
    return print(introduction)


if __name__ == "__main__":
    print_variables("a", "b")  # returns var1='a' var2='b'

    the_func('hello', thing='world')  # returns hello world
    the_func('world', 'hello')  # returns world hello
    the_func(greeting='hello', thing='world')  # returns hello world
    the_func(thing="world", greeting="hello")  # returns hello world
    the_func('hello', thing='world')  # returns hello world

    multiply(1, 2)  # returns 1 * 2 => 2
    multiply(1, 2, 3, 4)  # returns 1 * 2 * 3 * 4 => 24

    introduce(firstname='mike', lastname='huls')  # returns I am Mike Huls
    introduce(firstname='mike', lastname='huls', age=33, website='mikehuls.com')  # returns I am Mike Huls my age is 33 my website is mikehuls.com

