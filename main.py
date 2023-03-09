"""
These examples came from:
https://medium.com/towards-data-science/python-args-kwargs-and-all-other-ways-to-pass-arguments-to-your-function-bd2acdce72b5
"""


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
    :param args: unlimited number of additional numeric values
    :return: printed multiplied result
    """
    result = a * b
    for arg in args:
        result *= arg
    return print(result)


if __name__ == "__main__":
    the_func('hello', thing='world')  # returns hello world
    the_func('world', 'hello')  # returns world hello
    the_func(greeting='hello', thing='world')  # returns hello world
    the_func(thing="world", greeting="hello")  # returns hello world
    the_func('hello', thing='world')  # returns hello world

    multiply(1, 2)  # returns 1 * 2 => 2
    multiply(1, 2, 3, 4)  # returns 1 * 2 * 3 * 4 => 24
