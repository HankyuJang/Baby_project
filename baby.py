from data_clean import *
from menu import *

baby_label, baby_list = readcsv("data/NationalNames.csv")
baby_dict = list_to_dict(baby_list, 5)

menu(baby_dict)
