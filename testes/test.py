#!/usr/bin/env python3

numbers = [1, 2, 3, 4, 5, 6]
squares = [x ** 2 for x in numbers if x % 2 == 0]
print(squares)