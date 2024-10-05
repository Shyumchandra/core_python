from collections import ChainMap
c1={'a':1,'b':2}
c2={'b':3,'c':4}
chain_map=ChainMap(c1,c2)
print(chain_map)

print()

print(chain_map['b'])
chain_map['b']=5
chain_map['d']=2
print(chain_map['b'])

print()

for key in chain_map:
    print(key)
print()    
for value in chain_map.values():
    print(value)
print()    
for key,value in chain_map.items():
    print(key,value)        