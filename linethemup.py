def main():
    players = int(input())
    name1 = input()
    name2 = input()
    increasing = False
    decreasing = False
    if name1 < name2:
        increasing = True
    else:
        decreasing = True
    for x in range(players-2):
        name3 = input()
        if increasing and not (name2<name3):
            increasing = False;
        if decreasing and not (name2 > name3):
            decreasing = False
        name2 = name3

    if increasing:
        print("INCREASING")
    elif decreasing:
        print("DECREASING")
    else:
        print("NEITHER")

main()
