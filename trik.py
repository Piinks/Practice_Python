def main():
    ball = 1
    #print(ball)
    pattern = input()
    for x in range(len(pattern)):
        if(pattern[x]=='A' and (ball == 1 or ball == 2)):
            if ball == 1:
                ball = 2
            else:
                ball = 1
            #print(ball)
        if(pattern[x]=='B' and (ball == 2 or ball == 3)):
            if ball == 2:
                ball = 3
            else:
                ball = 2
            #print(ball)
        if(pattern[x]=='C' and (ball == 1 or ball == 3)):
            if ball == 1:
                ball = 3
            else:
                ball = 1
            #print(ball)
    print(ball)

main()
