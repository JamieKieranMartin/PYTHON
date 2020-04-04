
def t1():
    x = 0
    for i in range(1, 10):
        for j in range(1, i):
            x += 1
    return x

if __name__ == "__main__":
    print(t1())