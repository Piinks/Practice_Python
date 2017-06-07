# Recipe Scaling


def main():
    numRec = int(input())
    for x in range(numRec):
        details = input().split()
        numIngrd = int(details[0])
        startPortion = int(details[1])
        endPortion = int(details[2])

        scale = endPortion/startPortion
        ingreds = []
        scaledWeight = 0

        for y in range(numIngrd):
            ingreds.append(input().split())
            if float(ingreds[y][2]) == 100.0:
                scaledWeight = float(ingreds[y][1]) * scale
                ingreds[y][1] = scaledWeight

        print("Recipe #", x+1)

        #print(scaledWeight)
        for y in range(numIngrd):
            if float(ingreds[y][2]) != 100.0:
                print(ingreds[y][0], format((float(ingreds[y][2])*scaledWeight)/100.0, '.1f'))
            else:
                print(ingreds[y][0], format(scaledWeight, '.1f'))
        printBar()

def printBar():
    for x in range(40):
        print("-", end = '')
    print()

main()
