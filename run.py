import math



def cube_integer(number):
    """ Return the cube of an integer

    """

    return number ** 3

def diff_of_two_integers(int_one, int_two):
    """ Return the difference of two cubes

    """

    return abs(int_one - int_two)

def pair_generator(previous_number):
    """ Returns a pair of two consecutive numbers as a tuple. It is
    used to chain pairs of numbers for testing a prime number tester

    """

    return (previous_number, previous_number + 1)

def isPrime(num):
    """Returns True if num is a prime number, otherwise False.
    """

    # all numbers less than 2 are not prime
    if num < 2:
        return False

    # see if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def check_pair_differnce_prime(base_number):
    number_pair = pair_generator(base_number)
    result = isPrime(
        diff_of_two_integers(
            cube_integer(number_pair[0]),
            cube_integer(number_pair[1])
        )
    )

    # print("Number pair {} is {}".format(
    #     number_pair,
    #     result
    #     )
    # )

    return result



if __name__ == "__main__":
    true_total = 0

    end_of_range = int(input("How high would you like me to count?\n> "))

    for i in range(3,end_of_range):
        result = check_pair_differnce_prime(i)
        if result == True:
            true_total += 1

    print("\n{}% were prime numbers".format(
        (true_total / end_of_range) * 100
    ))
