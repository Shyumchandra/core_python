from collections import UserString

class MyString(UserString):
    def __add__(self, other):
        return self.data.upper() + other.data.upper()

my_string = MyString("hello")
result = my_string + " world"
print(result)  # Output: HELLO WORLD