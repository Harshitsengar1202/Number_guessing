import math

def search(array,guess):
    low=array[0]
    high=array[len(array)-1]
    mid=math.floor((low+high)/2)
    if mid<guess:
        low=mid
        print("The new range to guess is between:",low,"&",high)
    return mid



lr=int(input("Enter the lower range:"))
ur=int(input("Enter upper range:"))
temp=[]
for i in range(lr,ur+1):
    temp.append(i)
guess=int(input("ENter your guess:"))
out=search(temp,guess)
print(out)
#search(temp,guess)