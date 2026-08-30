num0=int(input("pls enter the amount of prime numbers you would like to know: "))
num1=2
start=2
count=0
while(count<=num0):
    num2=round(num1//2)
    
    if(num1 % start == 0): 
   
        num1 = num1 + 1
        start = 2
        
    elif(start>num2):
        print(num1, "->prime number")
        num1 = num1 + 1
        count=count+1
            
    else:
        start=start+1