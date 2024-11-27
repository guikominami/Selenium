from calculator import sum

try:
    print(sum(1, 'a'))
except AssertionError:
    print('invalid sum')