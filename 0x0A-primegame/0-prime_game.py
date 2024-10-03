#!/usr/bin/python3
"""
Define isWinner function, a solution to the Prime Game problem
"""


def sieve_of_eratosthenes(n):
    """Return a list of prime numbers up to n inclusive.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    prime_count = sieve_of_eratosthenes(max_n)
    maria_wins, ben_wins = 0, 0

    for n in nums:
        if len(prime_count[:n]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
