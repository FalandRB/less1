# Simple generator
def counter(n):
    i = 1
    while True:
        yield i
        if i == 1:
            i += 1
        else:
            i = 1
