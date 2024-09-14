
def add(*args):
    result = 1
    for i in args:
        result *= i
    return result

def oddOrNot(x):
    if x % 2 == 0:
        return True
    return False

result = add(4, 3)


print(oddOrNot(result))
