# Converter group project

import sys

class Unit:
    def __init__(self, unitname, convertto, factor):
        self.unitname = unitname
        self.convertto = convertto
        self.factor = factor

def _m(factor): return lambda v: v * factor

Unit.conversions = [Unit('kg', ['lbs', 'oz', 'g'], [_m(2.205), _m(35.274), _m(1000)]),
                    Unit('lbs', ['kg', 'oz', 'g'], [_m(.4535), _m(16), _m(453.592)]),
                    Unit('l', ['oz', 'fl oz'], [_m(33.814), _m(33.814)]),
                    Unit('c', ['f'], [lambda c: c * 1.8 + 32]),
                    Unit('f', ['c'], [lambda f: (f - 32) * .5555])]

def convert(s):
    [from_, to_] = s.split(' to ')

    # Add more units for conversion here:
    # , Unit('X', ['X','X'], [value, value])
    for i in Unit.conversions:
        if from_.endswith(i.unitname):
            val = float(from_.removesuffix(i.unitname))
            ind = i.convertto.index(to_)
            res = i.factor[ind](val)
            return f'{from_} is {res:.1f}{i.convertto[ind]}'

def parse(args):
    result = ''

    for arg in args:
        result += arg.lower() + " "

    return result.removesuffix(' ')

if __name__ == "__main__":

    try:
        val = parse(sys.argv[1:])
        result = convert(val)
        print(result)
    except Exception as e:
        print(e)
