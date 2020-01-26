#!/usr/bin/env python3
from numpy import linalg as l


def main():
    A = [list(map(float, input().strip().split(" "))) for _ in range(2)]
    try:
        res = l.inv(A)
    except l.LinAlgError:
        print("dunno")
    else:
        print("yes")


if __name__ == '__main__':
    main()
