n = int(input("enter the number of input:"))
arr = []

for i in range(1,n+1,1):
    t = input("n:")
    arr.append(t)
    
def insertion():

    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key

    print(arr)

insertion()
