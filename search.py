def number_of_babies(baby_dict, name, year, gender):
    """ Find number of babies when name, year, gender is given.

    name: string,
    year: int(ex 1880)
    gender: char(M or F)

    When grouped by 5 years,
    >>> baby_dict[('Mary', 1880, 'F')]
    39361
    """
    return baby_dict[(name, year, gender)]

def top_babies_helper(baby_dict, year, gender):
    """ Given year and gender, find a baby tuple
    which it's name is mostly used.

    When grouped by 5 years,
    >>> top_babies_helper(baby_dict, 2000, 'M')
    ('Jacob', 2000, 'M')
    >>> top_babies_helper(baby_dict, 2000, 'F')
    ('Emily', 2000, 'F')
    """
    baby_max = ('None', 0, gender)
    baby_count = 0
    for baby in baby_dict:
        if gender == baby[2] and year == baby[1] \
            and baby_dict[baby] > baby_count:
            baby_max = baby
            baby_count = baby_dict[baby]
    return baby_max

def top_named_babies(baby_dict, year, gender):
    """ Given year and gender, find a baby's name and number
    which it's name is mostly used.

    When grouped by 5 years,
    >>> top_named_babies(baby_dict, 1880, 'F')
    ('Mary', 39361)
    >>> top_named_babies(baby_dict, 2000, 'F')
    ('Emily', 126171)
    """
    baby_tuple = top_babies_helper(baby_dict, year, gender)
    return baby_tuple[0], baby_dict[baby_tuple]
