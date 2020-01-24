#!/usr/bin/env python3
from functools import reduce


def main():
    m, n = list(map(int, input().strip().split(" ")))
    A = [list(map(float, input().strip().split(" "))) for _ in range(m)]
    v = [float(input()) for _ in range(n)]

    w = [reduce(lambda x, y: x + y, map(lambda x, y: x * y, A[row], v)) for row in range(len(A))]
    print(*(f"{i:.12f}" for i in w))


if __name__ == '__main__':
    main()
