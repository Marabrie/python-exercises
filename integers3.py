user = int(input("Insert a number: "))

​def sum_func(user):
    #take user data turn into range
    range_of_numbers = [x for x in range(user + 1)]
    #then take sum of all integers
    total = sum(range_of_numbers)
    # sum(range(user))
    print(total)
​
​
sum_func(user)