n = int(input("enter the number of input:"))
arr = []
desc = int(input("Do you want sorting in descending order: yes(1) or No(0)"))

#Getting the input of array
for i in range(1,n+1,1):
    t = int(input("n:"))
    arr.append(t)
    
def bubbleSort():
    
    nos = 0
    print(f'input array:{arr}')
    for i in range(n):
        
        for j in range (0,n-i-1):
            
            if desc == 0:
                
                if  arr[j]<arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    nos = nos+1
            else:
                
                if  arr[j]<arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    nos = nos+1
                
    print(f'number of swapping :{nos}')
    print(arr)

bubbleSort()
