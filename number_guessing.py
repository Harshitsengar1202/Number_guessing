import math
import random
import time

def search(array,low,high,num):
    guess=int(input("Enter your guess:"))
    low=low
    high=high
    mid=math.floor((low+high)/2)
    if num<guess:
        if num<mid:
            high=mid
            print("The number is too far!!")
            print("The new range to guess is between:",low,"&",high)
            search(array,low,high,num)
        else:
            low=mid
            print("The number is too low!!")
            print("The new range to guess is between:",low,"&",high)
            search(array,low,high,num)
    elif num>guess:
        if num>mid:
            low=mid
            print("The number is too low!!")
            print("The new range to guess is between:",low,"&",high)
            search(array,low,high,num)
        else:
            high=mid
            print("The number is too far!!")
            print("The new range to guess is between:",low,"&",high)
            search(array,low,high,num)
    
    else:
        print("Congratulations you guessed it right!!!!!")



lr=int(input("Enter the lower range:"))
ur=int(input("Enter upper range:"))
temp=[]
for i in range(lr,ur+1):
    temp.append(i)
print("The system is choosing a random number between the range.......")
time.sleep(3)
print("The system has choosen it's number...")
num=random.randint(lr,ur)
#print(num)
low=temp[0]
high=temp[len(temp)-1]
search(temp,low,high,num)