# Mixed Fractions

def main():
    entries = input().split()
    numerator = int(entries[0])
    denominator = int(entries[1])

    while denominator != 0:
        integer = numerator // denominator
        newNumerator = numerator % denominator

        print(integer, newNumerator, '/', denominator)

        entries = input().split()
        numerator = int(entries[0])
        denominator = int(entries[1])

main()
