from collections import Counter
counter=Counter('Hello world')
print(counter)
print()

count_h=counter['h']
print(count_h)
print()

counter.update('hello girl')
print(counter)
print()

set1=Counter('abc')
set2=Counter('def')
add=set1+set2
diff=set1-set2
print(add)
print(diff)
print()

for key,value in counter.items():
    print(key,value)
print()    

most_common_elements=counter.most_common(2)
print(most_common_elements)
print()

#word tokenization
word="this is a sample sentence buddy!"
strings=Counter(word.split())
print(strings)