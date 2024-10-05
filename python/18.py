from collections import UserDict
class MyClass(UserDict):
    def __setitem__(self, key, value):
        if value > 0:
            super().__setitem__(key, value)
        else:
            print("Value must be positive")
dict=MyClass()
dict['X']=10
dict['Y']=-5            