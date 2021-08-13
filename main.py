x = int(input("enter the number"))
i = 0

while x != 1:
    if x % 2==0:
        x = x//2
    else:
        x = x * 3 + 1
    i = i+1
    
            
    print(x)
print(f"the no of steps ={i}")
        
