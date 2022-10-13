import sys

def readInput():
    a, b = sys.stdin.readline().strip("\n").split(" ")
    return int(a), int(b)


def sol(a, b):
    return a*b / ([x for x in range(1, a+1) if a%x==0 and b%x==0][-1])


def main():
    a, b = readInput()
    print(int(sol(a,b)))



if __name__ == "__main__":
    main()