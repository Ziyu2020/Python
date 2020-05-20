def gcd(x,y):
    """the minimal factor"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(y, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x,y):
    """the least common multiple"""
    common_multiple = x * y // gcd(x,y)
    return common_multiple


x = int(input('x = '))
y = int(input('y = '))
print('the minimal of them is %d, the least common multiple is %d' % (gcd(x,y), lcm(x,y)))

def is_prime(x):
    for factor in range(2,x):
        if x % factor == 0:
            return False
    return True if x != 1 else False

a = int(input('please insert a number a = '))
print('the number is prime? ', is_prime(a))
