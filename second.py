import random
l=["apple","banana","pineapple","grapes","mangoes"]
word=random.choice(l)
print(word)
length=[]
for i in word:
    length.append('_')
print(f"length is {length}")
cond=False
lives=len(word)
while not cond:
    count=0
    letter=input("enter letter:")
    for i in range(0,len(word)):
        search=word[i]
        if search==letter:
            length[i]=letter
            print(length)
            count=1
    if count==0:
        lives-=1
        if lives==0:
            cond=True
            print("you lose")
    if "_" not in length:
        print("you win")
        cond=True
    


    