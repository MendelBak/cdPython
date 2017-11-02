def draw_stars2(list):
    """Draw stars (*) based on the value of each integer or length of string in the list provided as a variable."""
    for i in list:
      if type(i) is int:
          int_counter = i
          print "*" * int_counter
      elif type(i) is str:
        str_counter = len(i)
        """Next, convert to lowercase and print first letter as many times as letters in that word"""
        new_str = i.lower()
        print new_str [0] * str_counter

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)