word=input("enter word:")
while True:
    count=0
    guess=input("enter letter:")
    for i in range(0,len(word)):
        if (guess==word[i]):
           count+=1
    if count>0:
        print("letter is in word")
        print(count)
    else:
        print("letter is not in word")
        print(count)