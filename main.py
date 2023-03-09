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


def multiply(a: int, b: int, *args: int):
    """
    Function multiplies arguments together
        Requires at least two integer values (a, b) and accepts an unlimited additional number of integer values
    :param a: numeric
    :param b: numeric
    :param args: tuple of unlimited number of additional integer values
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


def transfer_money(*, from_account: str, to_account: str, amount: int):
    """
    Only accept named arguments
    :param from_account: account to pull funds from
    :param to_account: account to send funds to
    :param amount: amount to be transferred
    :return: printed statement describing what is happening
    """
    return print(f"Transferring ${amount} from {from_account} to {to_account}")


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
    introduce(firstname='mike', lastname='huls', age=33,
              website='mikehuls.com')  # returns I am Mike Huls my age is 33 my website is mikehuls.com

    transfer_money(from_account='1234', to_account='6578', amount=9999)
    # transfer_money('1234', '6789', 12345)  # returns error because function requires keyword arguments

