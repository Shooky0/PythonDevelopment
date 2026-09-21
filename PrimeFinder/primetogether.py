

while True:
    try:
        print("PYTHON PRIME NUMBER FINDER")
        print("Available options:")
        print("1.Find whether 'x' is prime or composite")
        print("2.Find prime and composite numbers till 'x'")
        print("3.Find 'x' prime numbers")
        user_input=int(input("Please enter the specified program to run: "))
        if 1 <= user_input <= 3:
            break
        else:
            print("The input must be from given inputs. Retrying...")

    except Exception:
        print("Input must be a valid number. Retrying...")

if(user_input==1):
    while True:
        try:
            num1 = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    factor_pairs = []
    if num1 < 2:
        print(num1, "is neither prime nor composite.")
    else:
        for factor in range(2, int(num1 ** 0.5) + 1):
            if num1 % factor == 0:
                factor_pairs.append((factor, num1 // factor))

        if not factor_pairs:
            print(num1, "is a prime number")
        else:
            print(num1, "is a composite number")
            print("Factor pairs:")
            for a, b in factor_pairs:
                print(f"{a} X {b}")

if(user_input==3):
    while True:
            try:
            # Try to convert the input to an integer
                num0 = int(input("Please enter the amount of numbers you would like to know: "))
            # If successful, break out of the loop
                break
            except ValueError:
            # If it fails (e.g., they typed "hello" or "3.14"), print an error and loop again
                print("Invalid input. Please enter a whole number.Retrying...")
    num1=2
    start=2
    t=0
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
if(user_input==2):
    while True:
               try:
               # Try to convert the input to an integer
                   num0 = int(input("Please enter the amount of prime numbers you would like to know: "))
               # If successful, break out of the loop
                   break
               except ValueError:
               # If it fails (e.g., they typed "hello" or "3.14"), print an error and loop again
                   print("Invalid input. Please enter a whole number.Retrying...")
    num1=2
    start=2
    while(num1<=num0):
        num2=round(num1//2)
    
        if(num1 % start == 0): 
            print(num1,"->composite,",num1,"=",start,"X",num1//start)
            num1 = num1 + 1
            start = 2
        
        elif(start>num2):
            print(num1, "->prime number")
            num1 = num1 + 1
        
            
        else:
            start=start+1

