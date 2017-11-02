users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def names2(names_dict):
    for group_title in names_dict: #Instructors and Students
        print group_title
        group_list = names_dict[group_title] #Contains all the objects in each section
        for count, person in enumerate(group_list, start=1): #All of the separate objects in the dictionary
            print count, "-", person ["first_name"].upper(), person["last_name"].upper(), "-", len(person["first_name"]) + len(person["last_name"])
names2(users)