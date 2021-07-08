class Food():
    def __init__(self):
        pass

def check_if_same(x, y):
    if x is y:
        return x is y
    else:
        return x is y
    
f1 = Food()
same_f = f1

f2 = Food()
another_f = f2


print(check_if_same(f1, same_f))
print(check_if_same(same_f, another_f))
