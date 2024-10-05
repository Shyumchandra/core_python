dict={'name':'hello','age':20,'city':'hyd'}
dic={}
print(dict)
print(dict['name'])
dict['age']=30
print(dict)
dict['id']=12342
print(dict)
del dict['age']
print(dict)

print()

if 'name' in dict:
    print('key exists')
    
print(dict.keys())
print(dict.values())
print(dict.items())

print()

print(dict.get('na',"NOT FOUND"))
dict.update({'ph':'1234567890'})
print(dict)
print(dict.pop('name','NOT FOUND'))
dict.clear()
print(dict)