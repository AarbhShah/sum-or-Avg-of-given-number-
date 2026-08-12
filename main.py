def total(*Num):
    sum = 0
    for i in Num:
        sum = sum + i
    return sum
    
def avg(*Num):
    x = total(*Num)
    y = len(Num)
    avg = x/y
    return avg
    
    
    
    
y = []
print("Enter 0 for end")
while True:
         try:
             x = int(input("Enter the number:\t"))
         except:
             print("invalid Number\n ")
             continue
         if(x == 0):
             print("\n")
             break
         y.append(x)
    

print(*y,sep ="+")

print(f"Total = {total(*y)}")
print(f"Average = {avg(*y)}")