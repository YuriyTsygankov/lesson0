my_dict = {'Ivan': 1972, 'Yuriy': 1962, 'Anatoliy': 1952, 'Serg': 1968}
print('Dict:', my_dict)
print('Existing value:', my_dict['Ivan'])
print('Not existing value:', my_dict.get('Alex'))
my_dict.update({'Alex': 2007,
                'Maxim': 2006})
print(my_dict)
print('Deleted value:', my_dict['Ivan'])
del my_dict['Ivan']
print('Modified dictionary:', my_dict)
my_set = {7, 7, 7, 7, 7, 7, 7, 7, 3.14159, 3.14159, 'Pi', 'Pi', 'Pi', 'Pi'}
print('Set:', my_set)
my_set.remove(7)
my_set.add((5, 6, 1.2345))
my_set.add(8)
print('Modified set:', my_set)
