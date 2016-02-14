def readcsv(filename):
    """ This function reads data from csv formatted file.

    1. Save the first line into a tuple.
    >>> baby_label
    ('Name', 'Year', 'Gender', 'Count')

    2. Save the baby data to a list of tuples.
    >>> baby_list[0]
    ('Mary', 1880, 'F', 7065)
    >>> baby_list[1]
    ('Anna', 1880, 'F', 2604)
    """
    nameHandle = open(filename, 'r')
    baby_list = []
    # Get the label
    line = nameHandle.readline()
    line = line.rstrip()
    baby = line.split(',')
    baby_label = tuple(baby[1:])
    # Get babies
    for line in nameHandle:
        line = line.rstrip()
        baby = line.split(',')
        baby[2] = int(baby[2])
        baby[4] = int(baby[4])
        baby_list.append(tuple(baby[1:]))
    nameHandle.close()
    return baby_label, baby_list

def list_to_dict(L, year):
    """ Make a dictionary that groups babies with
    same name and gender with given amount of years
    starting from 1880.

    if year == 5, then
        ('Mary', 1880, 'F', 7065)
        ('Mary', 1881, 'F', 6919)
        ('Mary', 1882, 'F', 8148)
        ('Mary', 1883, 'F', 8012)
        ('Mary', 1884, 'F', 9217)
    would be grouped into
        key: [('Mary', 1880, 'F')]
        value: 39361
    """
    baby_dict = {}
    for baby in L:
        if baby[1] % year == 0:
            baby_dict[baby[:3]] = baby[3]
        elif (baby[0], round(baby[1], -1), baby[2]) in baby_dict:
            baby_dict[(baby[0], round(baby[1], -1), baby[2])] += baby[3]
        else:
            baby_dict[(baby[0], round(baby[1], -1), baby[2])] = baby[3]
    return baby_dict
