def main():
    total = 0
    numAddends = int(input())
    for x in range(numAddends):
        origNum = input()
        power = int(origNum[-1])
        num= int(origNum[0:(len(origNum)-1)])
        currResult = num**power
        total+=currResult
    print(total)

main()
