import random
l=["apple","banana","pineapple","grapes","mangoes"]
word=random.choice(l)
print(word)
length=[]
for i in word:
    length.append('_')
print(length)
