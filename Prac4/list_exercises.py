def main():
    numbers = []
    for i in range(5):
        number = int(input("Number:"))
        numbers.append(number)
    listoperations(numbers)
    name_checker()

def listoperations(numbers):
    for j in numbers:
        print("Number:",j)

    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average number is", sum(numbers)/len(numbers))


def name_checker():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    askName = input("Username:")
    if askName in usernames:
        print("access granted")
    else:
        print("Access denied")


main()
