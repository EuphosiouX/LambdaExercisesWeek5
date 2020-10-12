sum = lambda x:x+15

x = int(input("Pick a number for x: "))
print("ADDITION\n""x:",x)
print("x+15:",sum(x),"\n")


multiple = lambda x,y:x*y

y = int(input("Pick a number for y: "))
print("MULTIPLICATION\n""x:",sum(x),"\n""y:",y)
print("x*y:",multiple(sum(x),y))