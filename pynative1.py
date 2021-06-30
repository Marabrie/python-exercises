keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

samplenumberDict= dict(zip(keys, values))
print (samplenumberDict)



dict1 = {'Ten':10, 'Twenty':20, 'Thirty':30}
dict2 = { 'Thirty':30.0, 'Fourty': 40, 'Fifty':50}

dict3 = {**dict1, **dict2}
print(dict3)

dict1 = {'Ten': 10,'Twenty':20, 'Thirty':30} 
dict2 = {'Thirty':30,'Fourty': 40, 'Fifty':50}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
