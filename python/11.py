from collections import defaultdict
num=defaultdict(int)

list_=defaultdict(list)

class Myclass:
    pass
class_=defaultdict(Myclass)

sample="This is a sample text. This text has some repeated words."
text=defaultdict(int)

for word in sample.split():
    text[word]+=1
print(text)    
