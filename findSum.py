# Find the sum from a list of numbers

from sys import stdin

def main():
    for line in stdin:
        if line == '\n':
            break
        line = line.split()
        for x in range(len(line)):
            potSum = int(line[x])
            testSum = 0
            for y in range(len(line)):
                if x==y:
                    continue
                else:
                    testSum += int(line[y])
            if potSum == testSum:
                print(potSum)
                break



main()
