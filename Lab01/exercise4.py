# exercise 4


def removeThenPrint(string):
    result = ""
    splited_string = string.split()
    for string in splited_string:
        result = result + string.strip()
    print(result)


def replaceThenPrint(string):
    string = string.strip()
    print(string.replace(" ", "_"))


string = input()
removeThenPrint(string)
replaceThenPrint(string)
