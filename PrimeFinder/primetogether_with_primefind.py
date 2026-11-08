from Primefind import isprime, primes_till_that_num, that_many_primes


def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
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
        elif isprime(num):
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
        prime_numbers = set(primes_till_that_num(limit + 1))
        for candidate in range(2, limit + 1):
            if candidate in prime_numbers:
                print(f"{candidate} -> prime number")
            else:
                print(f"{candidate} -> composite number")

    elif user_input == 3:
        total = get_valid_int("Please enter how many prime numbers you would like to know: ")
        for prime in that_many_primes(total):
            print(f"{prime} -> prime number")


if __name__ == "__main__":
    main()
