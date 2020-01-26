#!/usr/bin/env python3


def norm1(A):
    return max([sum(list(map(abs, i))) for i in zip(*A)])


def normInf(A):
    return max([sum(list(map(abs, i))) for i in A])


def inverse(A):
    n = len(A)
    R = [[0.0 for _ in range(n * 2)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            R[i][j] = A[i][j]

    for i in range(n):
        for j in range(n, n * 2):
            if i == (j - n):
                R[i][j] = 1

    for i in range(n):
        while R[i][i] == 0:
            R[i], R[i + 2] = R[i + 2], R[i]
        t = R[i][i]
        for j in range(i, 2 * n):
            R[i][j] = R[i][j] / t
        for j in range(n):
            if i != j:
                t = R[j][i]
                for k in range(2 * n):
                    R[j][k] -= t * R[i][k]

    for i in range(n * n):
        R[int(i / n)].pop(0)

    return R


def main():
    n = int(input())
    A = [list(map(float, input().strip().split(" "))) for _ in range(n)]
    invA = inverse(A)

    infA = normInf(A) * normInf(invA)
    oneA = norm1(A) * norm1(invA)

    print(f"{round(infA, 12):.12f} {round(oneA, 12):.12f}")


if __name__ == '__main__':
    main()
