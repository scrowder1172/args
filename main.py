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


def only_positional_arguments(arg1: str, arg2: str, /):
    """
    Example of functionl only allowing positional arguments
        Similar to len() which doesn't allow  keyword/named argument
    :param arg1: first value
    :param arg2: second value
    :return: printed statement with argument names and values
    """
    return print(f"{arg1=} {arg2=}")


def exceeds_100_bytes(x, /) -> bool:
    """
    Check if argument total size is over 100 bytes
        Return true if >100 bytes
        Return false if !>100 bytes
    Only accepts positional argument
    :param x: value to check
    :return: boolean
    """
    return x.__sizeof__() > 100


def exceeds_100_bytes_unlimited(*args) -> bool:
    for a in args:
        if a.__sizeof__() > 100:
            return True
    return False


def len_new(x, /, *, no_duplicates=False):
    """
    Function checks the length of the first argument
    If no_duplicates=True then function removes duplicate values and then checks length
    :param x: value to check length of
    :param no_duplicates: whether to ignore duplicates
    :return: length of argument
    """
    if no_duplicates:
        return print(len(list(set([a for a in x]))))
    return print(len(x))


def pos_or_kw(pos_only1, pos_only2, /, pos_or_kw1, pos_or_kw2, *, kw1, kw2, **extra_kw):
    """
    Generate a printed statement with all the arguments and their values
        If extra_kw is included then the additional arguments are printed as a dictionary
    :param pos_only1: unnamed argument
    :param pos_only2: unnamed argument
    :param pos_or_kw1: named or unnamed argument
    :param pos_or_kw2: named or unnamed argument
    :param kw1: named argument
    :param kw2: named argument
    :param extra_kw: unlimited additional named arguments
    :return: printed statement of each argument and value
    """
    print(f"{pos_only1=}, {pos_only2=}, {pos_or_kw1=}, {pos_or_kw2=}, {kw1=}, {kw2=}, {extra_kw=}")


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

    only_positional_arguments('num1', 'num2')  # returns arg1='num1' arg2='num2'
    # only_positional_arguments(arg1="num1",
    #                           arg2="num2")  # returns error because function requires positional arguments

    print(exceeds_100_bytes('a'))  # returns False because size is less than 100 bytes
    print(exceeds_100_bytes({'a', 'b'}))  # returns True because size is greater than 100 bytes

    print(exceeds_100_bytes_unlimited(1, 2))  # returns False because no parameter is over 100 bytes
    print(exceeds_100_bytes_unlimited(1, 2, 484585))  # returns False because no parameter is over 100 bytes
    print(exceeds_100_bytes_unlimited(1, 2, 484585,
                                      {1, 2, 3, 4}))  # returns True because at least one parameter is >100 bytes

    len_new('abc')  # returns 3
    len_new('aabc')  # returns 4
    len_new('aabc', no_duplicates=True)  # returns 3
    # len_new(x='123')  # returns error because first parameter cannot be named

    pos_or_kw('1', '2', pos_or_kw1=3, pos_or_kw2=4, kw1=5, kw2=6, kw3=7,
              kw4=8)  # returns pos_only1='1', pos_only2='2', pos_or_kw1=3, pos_or_kw2=4, kw1=5, kw2=6, extra_kw={'kw3': 7, 'kw4': 8}
    # pos_or_kw(pos_only1=1, pos_or_kw1=3, pos_or_kw2=4, kw1=5, kw2=6,
    #           kw3=7)  # returns error because first two parameters cannot be named

