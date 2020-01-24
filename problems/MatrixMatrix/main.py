#!/usr/bin/env python3


def matrix_multiply(A, B):
    result = [[0.0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j] += A[i][k] * B[k][j]
    return result


def main():
    k, m, n = list(map(int, input().strip().split(" ")))
    A = [list(map(float, input().strip().split(" "))) for _ in range(k)]
    B = [list(map(float, input().strip().split(" "))) for _ in range(m)]

    result = matrix_multiply(A, B)

    for row in result:
        for elem in row:
            if int(elem) == float(elem):
                print(f"{elem:.0f}")
            else:
                print(f"{elem:.12f}")


if __name__ == '__main__':
    main()
