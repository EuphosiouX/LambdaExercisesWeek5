fibonacci = lambda x:x if x<=1 else fibonacci(x-1)+fibonacci(x-2)

while True:
    N = int(input("Pick a number of element: "))
    if(N<=0):
        print("Please enter number bigger than 0")
    else:
        for i in range(N):
            print(fibonacci(i))

