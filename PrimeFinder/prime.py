while True:
    try:
        # Try to convert the input to an integer
        num1 = int(input("Please enter a number: "))
        # If successful, break out of the loop
        break
    except ValueError:
        # If it fails (e.g., they typed "hello" or "3.14"), print an error and loop again
        print("Invalid input. Please enter a whole number.")

num2=num1//2
start=2
for i in range(num1):
    if(num1==num2*start):
        print(num2,"X",start)
        print("Hence,",num1,"is a composite,not a prime")
        break
    elif(start==num2):
        if(num1!=num2*start):
            print(num1,"is a prime number")
            break
        else:
            print(num2,"X",start)
            print("Hence,",num1,"is a composite,not a prime")
            break
    else:
        start=start+1