names = ["Adam", "Betty", "Charles", "David", "Edward", "Frank"]
apples = ["Gala", "Yellow Delicious", "Granny Smith", "HoneyCrisp", "Red (not) Delicious", "Lady"]

def make_dict_from_list(list1, list2):
        temp_dict = zip(names, apples)
        new_dict = dict(temp_dict)
        print new_dict

make_dict_from_list(names, apples)    