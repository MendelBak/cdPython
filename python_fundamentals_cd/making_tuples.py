my_dict = {
    "Mendel": "8472080883",
    "Home": "8471231234",
    "Work": "8479879876"
}

def dict_to_tuple(dict):
    for titles in my_dict:
        new_tuple = (titles, my_dict[titles])
        print(new_tuple)

dict_to_tuple(my_dict)