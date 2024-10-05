from collections import OrderedDict
dict_=OrderedDict()

dict_['1']='v1'
dict_['2']='v2'

v1=dict_['1']
print(v1)

print()

for key in dict_:
    print(key)
print()    
for value in dict_.values():
    print(value)
print()    
for key,value in dict_.items():
    print(key,value)
print()

dict_.move_to_end('2',last=False)
dict_.move_to_end('1',last=True)

print(dict_)        