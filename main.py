"""
These examples came from:
https://medium.com/towards-data-science/python-args-kwargs-and-all-other-ways-to-pass-arguments-to-your-function-bd2acdce72b5
"""


def the_func(greeting, thing):
    """
    Function that prints out a greeting to a thing
    :param greeting: greeting message
    :param thing: thing that gets greeted
    :return: None
    """
    print(f"{greeting} {thing}")


if __name__ == "__main__":
    the_func('hello', thing='world')  # returns hello world
    the_func('world', 'hello')  # returns world hello
    the_func(greeting='hello', thing='world')  # returns hello world
    the_func(thing="world", greeting="hello")  # returns hello world
    the_func('hello', thing='world')  # returns hello world
