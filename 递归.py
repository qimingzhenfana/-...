def hanoi(n, res, ass, to):
    if n == 1:
        print("move " + str(n) + " from " + res + " to " + to)
    else:
        hanoi(n - 1, res, to, ass)
        print("move " + str(n) + " from " + res + " to " + to)
        hanoi(n - 1, ass, res, to)


hanoi(3, "A", "B", "C")
