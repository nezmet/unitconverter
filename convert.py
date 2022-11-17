# Converter group project

import sys

class Unit:
    def __init__(self, unitname, convertto, factor):
        self.unitname = unitname
        self.convertto = convertto
        self.factor = factor

def convert(s):
    [from_, to_] = s.split(' to ')

    # Add more units for conversion here:
    for i in [Unit('kg',  ['lbs', 'oz', 'g'], [2.205, .0283, 1000]),
              Unit('lbs', ['oz',  'kg', 'g'], [16, .4535, .0022]),
              Unit('l', ['fl oz', 'oz'], [33.814, 33.814])]:
        if from_.endswith(i.unitname):
            val = float(from_.removesuffix(i.unitname))
            ind = i.convertto.index(to_)
            return f'{from_} is {val * i.factor[ind]:.2f}{i.convertto[ind]}'

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
    except:
        print("Incorrect syntax. Example: 10kg to lbs")
