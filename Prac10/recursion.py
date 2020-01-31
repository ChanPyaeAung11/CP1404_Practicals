"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# write down what you think the output of this will be,
# 3
#  use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)


# what I think the output of do_something(4) will be,
# 16, 9, 4, 1, 0
# use the debugger to step through and see what's actually happening
do_something(4)


def build_pyramid():
    chosen_rows = int(input("How many rows is your pyramid: "))
    print("For {} rows, you need {} blocks".format(chosen_rows, calculate_blocks(chosen_rows)))


def calculate_blocks(rows):
    """ Calculate the numbers of blocks needed by taking in a number and doing a n-1 formula and stops until n
    reaches 0 """
    if rows <= 0:
        return 0
    print(rows + calculate_blocks(rows - 1))
    return rows + calculate_blocks(rows - 1)


build_pyramid()
