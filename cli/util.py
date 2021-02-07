from functools import reduce


def pipe(*funcs):
    def apply(arg, func): return func(arg)
    def composition(x): return reduce(apply, [x, *funcs])
    return composition

def to_alias_text(alias_map, delimiter):
    """alias_map -> alias_text
    """
    alias_text = []
    for alias, path in alias_map.items():
        alias_text.append(f'{alias}{delimiter}{path}\n')

    return alias_text


def to_alias_map(alias_text, delimiter):
    """alias_text -> alias_map
    """
    alias_map = dict()

    for row in alias_text:
        alias, path = row.split(delimiter)
        alias_map[alias] = path

    return alias_map
