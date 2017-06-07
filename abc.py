#order me this

def main():
    nums = sorted(input().split())
    order = list(input())

    for letter in order:
        if letter == 'A':
            print(nums[0], end = ' ')
        elif letter == 'B':
            print(nums[1], end = ' ')
        elif letter == 'C':
            print(nums[2], end = ' ')

    print()

main()
