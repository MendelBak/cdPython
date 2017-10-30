#Find Characters

def findChars(str_list, search_str):
  new_list = []
  for i in range(0, len(str_list)):
  	if str_list[i].find(search_str) != -1:
  	  new_list.append(str_list[i])
  	  
  print new_list
		