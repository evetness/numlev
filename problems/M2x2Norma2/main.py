#!/usr/bin/env python3
from numpy import linalg as l


def main():
    A = [list(map(float, input().strip().split(" "))) for _ in range(2)]
    print(l.norm(A, 2))


if __name__ == '__main__':
    main()
