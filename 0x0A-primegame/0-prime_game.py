#!/usr/bin/python3
'''Prime Game'''

def is_prime(n):
    """
    Checks the number given if its a prime number
    """
    for a in range(2, int(n ** 0.5) + 1):
        if not n % a:
            return False
    return True


def find_primes(n, pnum):
    """
    Calculate all prime numbers in a
    """
    last_p = pnum[-1]
    if n > last_p:
        for i in range(last_p + 1, n + 1):
            if is_prime(i):
                pnum.append(i)
            else:
                pnum.append(0)


def isWinner(x, nums):
    """
    x is the number of turnss and nums is an array of n

    Return:
         name of the player that won the most turnss or None
    """

    score = {"Maria": 0, "Ben": 0}

    setOfPrimes = [0, 0, 2]

    # The first two elements are set to 0 because they are not prime numbers

    find_primes(max(nums), setOfPrimes)

    for turns in range(x):
        sum_options = sum((i != 0 and i <= nums[turns])
                          for i in setOfPrimes[:nums[turns] + 1])

        if (sum_options % 2):
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            score[winner] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"

    return None
