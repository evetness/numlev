#!/usr/bin/env python3


def main():
    d = int(input())
    v = list(map(float, input().strip().split(" ")))
    w = list(map(float, input().strip().split(" ")))
    data = [v[i] * w[i] for i in range(d)]

    print(f"{round(sum(data), 8):.12f}")


if __name__ == '__main__':
    main()
