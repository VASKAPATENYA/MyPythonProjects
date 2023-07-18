from pickle import TRUE


def prime(number):
    is_it_prime=True
    for i in range(2, number):
        if number%i == 0:
            is_it_prime=False
    if is_it_prime:
        print("prime number")
    else:
        print("not a prime number")
prime(int(input("Check This Number: ")))