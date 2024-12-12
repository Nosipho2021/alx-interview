#!/usr/bin/python3


def isWinner(x, nums):
    """Determines the winner of the prime game."""
    if not nums or x < 1:
        return None

    # Find the maximum value in nums
    max_num = max(nums)

    # Sieve of Eratosthenes to precompute primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime

    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Precompute the number of primes up to each number
    primes_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1] + (1 if sieve[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 1:  # Maria wins if odd primes
            maria_wins += 1
        else:  # Ben wins if even primes
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

