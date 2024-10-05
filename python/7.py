my_set={1,2,3,4}
print(my_set)

print()

my_set.add(5)
print(my_set)

print()

my_set.remove(3)
my_set.discard(6)
print(my_set)

print()

a={1,2,3}
b={4,5,6}
union_=a.union(b)
print(union_)
diff=a.difference(b)
print(diff)
inter=a.intersection(b)
print(inter)
sem_int=a.symmetric_difference(b)
print(sem_int)

print()

if 2 in a:
    print("2 in a")

print()

frozen_set=frozenset([1,2,3])   
print(frozen_set) 

