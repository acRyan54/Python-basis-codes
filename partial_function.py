import functools

def mod(x, y = 2):
    print(x % y == 0)

mod(4, y = 3)
mod(6, y = 3)

mod3 = functools.partial(mod, y = 3)

mod3(4)
mod3(6)