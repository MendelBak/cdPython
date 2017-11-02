def draw_stars(list):
    """Draw stars (*) based on the value of each integer in the list provided as a variable."""
    for i in list:
     counter = i
     print "*" * counter

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)