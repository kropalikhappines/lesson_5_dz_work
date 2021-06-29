def nums_gen():
    for i in range(1, 15 + 1, 2):
        yield i
            

g = nums_gen()
print(next(g))
print(next(g))
print(next(g))
