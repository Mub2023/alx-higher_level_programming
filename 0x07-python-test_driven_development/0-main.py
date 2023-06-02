#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
print(add_integer(100.3, -2))
print(add_integer(-100.3, 0))
print(add_integer(-100.3, -2))
try:
    print(add_integer('a', 0))
    print(add_integer('x', 42))
    print(add_integer(float('inf'), 0))
    print(add_integer(4, float('nan')))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
