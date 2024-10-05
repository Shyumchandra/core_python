mylist=[]
fruits=['apple','banana','watermelon']
num=[1,2,3,4,5,6]

print(fruits[1])
print(num[0])

fruits[1]='grapes'
print(fruits)
print(fruits[1:3])

print()

fruits.append('greenapple')
print(fruits)
fruits.insert(1,'pan')
print(fruits)

print()

fruits.pop()
print(fruits)
fruits.remove('apple')
print(fruits)

print()

print(len(fruits))

print()

squared_num=[x**2 for x in num]
print(squared_num)

print()

a=[1,3,2,6,4]
a.sort()
print(a)

print()

a.reverse()
print(a)

b=a.copy()
print(b)

print()

a.clear()
print(a)

