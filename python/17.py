from collections import UserList
class MyClass(UserList):
    def append(self,item):
        if item not in self.data:
            super().append(item)
my_class=MyClass([1,2,3])
my_class.append(3)
print(my_class)            