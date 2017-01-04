# Estimating the Area of a Circle
# Kate Archer

# Input: true radius, number of darts thrown, number of darts that landed in the circle
# Output: true area of the circle and the estimated area of the circle.

# Area of a circle is pi * radius^2
# estimate the area by calucating an estimated pi by 4 * (number of darts in / all darts thrown).
# Then multiply by given radius.

PI = 3.141592654

def main():
    given = input().split()

    if(int(given[1]) != 0):
        piEstimate = (int(given[2]) / int(given[1])) * 4

        realArea = (float(given[0])**2) * PI
        estArea = (float(given[0])**2) * piEstimate

        print(realArea, estArea)

main()
