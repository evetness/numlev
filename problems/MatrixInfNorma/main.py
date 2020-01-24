#!/usr/bin/env python3


def main():
    n = int(input())
    A = [list(map(float, input().strip().split(" "))) for _ in range(n)]
    norm = max([sum(list(map(abs, i))) for i in A])

    print(f"{round(norm, 8):.12f}")


if __name__ == '__main__':
    main()
