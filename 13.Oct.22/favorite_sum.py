import sys

def readInput():
    fav_count, x = sys.stdin.readline().split(" ")
    fav_numbers = sys.stdin.readline().strip("\n").split(" ")
    return int(x), list(map(int, fav_numbers))


def sol(x, fav_numbers):
    temp_sum = x*(x+1) //2
    filtered = list(filter(lambda a: a <= x, fav_numbers))
    final = temp_sum - sum(filtered) * 2
    return final

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        x, fav_numbers = readInput()
        s = sol(x, fav_numbers)
        print(s)

if __name__ == "__main__":
    main()