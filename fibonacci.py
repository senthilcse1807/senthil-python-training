num = int(input("Enter a number: "))

a, b = 0, 1

if num <= 0:
    print("Please enter a positive number.")
elif num == 1:
    print("Fibonacci series:", a)
else:
    print("Fibonacci series:")
    for i in range(num):
        print(a, end=" ")
        a, b = b, a + b
