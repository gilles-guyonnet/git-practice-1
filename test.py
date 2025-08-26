#!/usr/bin/env python
import os

if __name__ == '__main__':
    os.system('clear')

    result: float = 3.14 * 10
    print(f'The result is {result:.2f}')

    letters = ["a"]
    class Character:
        letters = ["b"]
        letters = letters + ["c"]

    print(letters[0], Character.letters)
    print("\nEnd")

