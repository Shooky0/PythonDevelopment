def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def is_prime(value):
    if value < 2:
        return False
    if value in (2, 3):
        return True
    if value % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


print("PYTHON PRIME NUMBER FINDER")
print("Available options:")
print("1.Find whether 'x' is prime or composite")
print("2.Find prime and composite numbers till 'x'")
print("3.Find 'x' prime numbers")

while True:
    try:
        user_input = get_valid_int("Please enter the specified program to run: ")
        if 1 <= user_input <= 3:
            break
        print("The input must be from given inputs. Retrying...")
    except Exception:
        print("Input must be a valid number. Retrying...")

if user_input == 1:
    num = get_valid_int("Please enter a number: ")
    if num < 2:
        print(num, "is neither prime nor composite.")
    elif is_prime(num):
        print(num, "is a prime number")
    else:
        print(num, "is a composite number")
        print("Factor pairs:")
        factor = 2
        while factor * factor <= num:
            if num % factor == 0:
                print(f"{factor} X {num // factor}")
            factor += 1

elif user_input == 2:
    limit = get_valid_int("Please enter the maximum number to check: ")
    for candidate in range(2, limit + 1):
        if is_prime(candidate):
            print(f"{candidate} -> prime number")
        else:
            print(f"{candidate} -> composite number")

elif user_input == 3:
    total = get_valid_int("Please enter how many prime numbers you would like to know: ")
    count = 0
    candidate = 2
    while count < total:
        if is_prime(candidate):
            print(f"{candidate} -> prime number")
            count += 1
        candidate += 1
