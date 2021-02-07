from functools import reduce


def pipe(*funcs):
    def apply(arg, func): return func(arg)
    def composition(x): return reduce(apply, [x, *funcs])
    return composition
