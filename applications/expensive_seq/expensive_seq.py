# Your code here
# Hint: In Python, a dict key can be any immutable type...
#       including a tuple.

cache = {}


def expensive_seq(x, y, z):
    # Your code here
    # exps will be our keys in the dict
    exps = (x, y, z)

    # x, y, and z are all greater than 0
    if x <= 0:
        return y + z

    if exps not in cache:
        cache[(x, y, z)] = expensive_seq(x-1, y+1, z) + \
            expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
    return cache[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
