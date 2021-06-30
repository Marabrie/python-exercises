print ("Welcome to Pypet!")

name =  ' Fluffy '
age = 5
weight = 9.5
hungry = True
photo = "<`)))><"

print('Hello' + name)
print(photo)

fish = {
'name': 'Fluffy',
'age': 5,
'weight' : 9.5,
'hungry' : True,
'photo' : "<`)))><",
}

mouse = {
    'name': 'Mouse',
    'age': 6,
    'weight': 1.5,
    'hungry': False,
    'photo': '<:3)~~~',
}

pets =[fish,mouse]
def feed(pet):
    if pet['hungry'] == True:
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 1    
    else:
        print('The Pypet is not hungry!')
for pet in pets:
    feed(pet)
    print(pet)

print(fish) 
feed(fish)
print(fish)
feed(fish)