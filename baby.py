from data_clean import *
from search import *

baby_label, baby_list = readcsv("data/NationalNames.csv")
baby_dict = list_to_dict(baby_list, 5)

print("Welcome to U.S. babies!")
print("-----------------------")
while True:
    print("\n< Options >")
    print("1. Search number of babies using name, year and gender")
    print("2. Search top ranked baby name")
    print("3. Exit")
    choice = input("What do you want to do? Type in a number: ")
    if choice == '1':
        name = input("name: ")
        year = int(input("year: "))
        gender = input("gender: ")
        try:
            baby = number_of_babies(baby_dict, name, year, gender.upper())
            print("\n", baby, "babies used this name")
        except:
            print("Try again.. error occured.")
    elif choice == '2':
        year = int(input("year(1880 ~ 2010): "))
        gender = input("gender(M or F): ")
        try:
            baby = top_named_babies(baby_dict, year, gender.upper())
            print("\nHere's the baby")
            print("name: ", baby[0])
            print("count: ", baby[1])
        except:
            print("Try again.. error occured.")
    elif choice == '3':
        print("See you again!")
        break
    else:
        print("Type in a number between 1 ~ 3")
        continue
