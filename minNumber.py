# Finding Minimum or SMALLEST number 
import random 

def min_number(arr):
    minNumber = arr[0]

    for i in range(len(arr)):
        if minNumber > arr[i]:
            minNumber = arr[i]
        else:
            minNumber = minNumber

    return minNumber


if __name__ == '__main__':
    arr = list()
    # Length of List
    n = int(input("Input the length of list : " ))
    
    for i in range(n):
        randomNumber = random.randint(1, n)
        arr.append(randomNumber)
    print(arr)
    print(min_number(arr))
