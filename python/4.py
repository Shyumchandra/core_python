str1='hi'
str2="babe"
str3="""You are
sexy"""
print(str1,str2,str3)
print(len(str1))
print(str1+str2)
print(str1*5)
print('babe' in str2)
print(str1 not in str2)

print()

str4="hello world"
print(str4[0])
print(str4[6:])
new_str=str4+"babe you are"
print(new_str)

print()

print(str4.upper())
print(str4.lower())
print(str4.capitalize())
print(str4.title())
print(str4.swapcase())
print(str4.find("world"))
print(str4.replace("world","hello"))
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())
print(str4.split())
print(str4.join(str2))