my_dictionary = {"name": "Mendel", "age": 22, "language": "Ivrit", "nation": "Judaism"}

def call_dictionary(dic):
    for keys, values in my_dictionary.iteritems():
        print "My {} is {}".format(keys, values)
call_dictionary(my_dictionary)