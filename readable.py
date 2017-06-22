#readability

def main ():
    name = input()
    result = ''
    priorLetter =''
    for char in name:
        if char != priorLetter:
            result += char
        priorLetter = char

    print(result)


main()
