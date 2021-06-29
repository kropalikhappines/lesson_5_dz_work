
def nums_gen():
    return (nums for nums in range(1, 15 + 1, 2))
g = nums_gen()
print(next(g))
print(next(g))
print(next(g))
