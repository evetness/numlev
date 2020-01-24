#!/usr/bin/env python3


def lu(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            res = (A[j][i] / A[i][i]) * -1
            for k in range(i, len(A)):
                A[j][k] = A[j][k] + (res * A[i][k])
            A[j][i] = res * -1
    return A


def main():
    n = int(input())
    A = [list(map(float, input().strip().split(" "))) for _ in range(n)]

    try:
        res = lu(A)
    except ZeroDivisionError:
        print("fail")
    else:
        for row in res:
            for elem in row:
                print(f"{elem:.12f}")


if __name__ == '__main__':
    main()
