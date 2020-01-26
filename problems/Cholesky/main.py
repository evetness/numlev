#!/usr/bin/env python3
from math import sqrt


def cholesky(A):
    L = [[0.0] * len(A) for _ in range(len(A))]
    for i, (Ai, Li) in enumerate(zip(A, L)):
        for j, Lj in enumerate(L[:i+1]):
            s = sum([Li[k] * Lj[k] for k in range(j)])
            try:
                Li[j] = sqrt(Ai[i] - s) if (i == j) else (1.0 / Lj[j] * (Ai[j] - s))
            except ZeroDivisionError:
                return "fail"
    return L


def main():
    n = int(input())
    M = [list(map(float, input().strip().split(" "))) for _ in range(n)]
    chol = cholesky(M)

    if "fail" in chol:
        print("fail")
    else:
        for i, row in enumerate(chol):
            print(f" ".join(filter(lambda x: x, map(str, map("{:.12f}".format, row[:int(i)+1])))))


if __name__ == '__main__':
    main()
