# Write a python function that takes a list of names and returns a new list
# with all the names that start with "Z" removed.
# test your function on this list:
# test_list = ['Zans', 'Dan', 'Grace', 'Zelda', 'L.E.', 'Zeke', 'Mara'] 

def remove_z(names):
    new_list = []
    # take names and look for names that start with Z
    # if name does not start with Z, put it into new_list.
    for name in names:
        if name[0] == 'Z':
            names.remove(name)
    print(names)

test_list = ['Zans', 'Dan', 'Grace','Zelda','L.E.','Zeke','Mara']
remove_z(test_list)

    