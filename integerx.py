#Write a function that takes an integer (x) 
#and then returns the sum of all positive integers 
#up to and including x.
#ex.my_function(6) would do
#1 + 2 + 3 + 4 + 5 + 6 and then return that answer

def sum_integers(number):
    
    return sum(range(0, number+1))

print(sum_integers(7))


