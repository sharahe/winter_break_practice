"""Libary that divides all numbers in a list by 10"""

def demo_list():
    # Lists
    my_list = [-50, -40, -30, -20, -10]
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(50)
    print(20 is my_list[6])

    for item in my_list:
        print(item)

    for i, item in enumerate(my_list):
        print("the {}th item of my_list is {}".format(i, item))

    # list comprehension
    [print(item) for item in my_list]

    # check if exists:
    if 0 in my_list:
        print("yay, 0 is there!")


# Dictionaries
def demo_dictionary():
    my_dict = {}
    my_dict['halloo'] = 10
    my_dict['there'] = 20
    my_dict['general'] = 30
    my_dict['kenobi'] = 40

    print(20 == my_dict['helloo'])

    for key in my_dict.keys():
        print(key)

    for key, value in my_dict.items():
        print("key: {}, value: {}".format(key, value))

    my_key = "balloo"
    if my_key in my_dict:
        print("balloo is there too!")


def demo_tuple():
    a = ('one', 'two')
    b = ('three', 'four', 'five')
    c, d, e = b

    # you also don't have to use all of the numbers from unpacking a tuple. If you don't care about
    # the second value, you could have just written: c, _, e = b and it just skips the second one
    print("c: {}, d: {}, e: {}".format(c, d, e))
    return 5, 6, 7


def div_by_ten(my_list):
    new_list = []
    for number in my_list:
        new_list.append(number / 10)

    return new_list


def int_div_by_ten(my_list):
    new_list = []
    for number in my_list:
        new_num = number / 10
        new_list.append(int(round(new_num)))
    return new_list


def empty_function():
    pass


if __name__ == '__main__':
    print(int_div_by_ten([10, 20, 30, 40]))
