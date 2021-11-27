# -*- encoding: utf-8 -*-

from random import randint

if __name__ == "__main__":
    li = [randint(0, 10) for _ in range(5)]
    print(f"Random Generated List: {li}")
