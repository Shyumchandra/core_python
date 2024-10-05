from collections import namedtuple
Person=namedtuple('Person',['name','age','gender'])
Person1=Person('shyum',20,'male')
print(Person1.age)
print(Person1.name)
print()

Person2=Person1._replace(age=21)
print(Person2.name,Person2.age)
print()

Book=namedtuple('Book',['name','author','year'])
books=[
    Book('harping','ajay',2004),
    Book('garaga','pradam',1900)
]
for book in books:
    print(book.name,'by',book.author,'in',book.year)