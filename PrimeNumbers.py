import math


def sieve_of_eratosthenes(n):
    """Generate all prime numbers below n using the Sieve of Eratosthenes."""
    if n < 2:
        return []

    # Initialize a boolean array to track primes
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Sieve of Eratosthenes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i * i, n, i):
                is_prime[j] = False

    # Extract prime numbers
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

def first_k_primes(k):
    if k == 0:
        return []
    
    # Estimate an upper bound for the k-th prime (tight formula)
    if k < 6:
        n = 15  # small manual value
    else:
        n = int(k * (math.log(k) + math.log(math.log(k)))) + 10  # a bit more than needed
    
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False

    primes = []

    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
            if len(primes) == k:
                break
            for j in range(i*i, n+1, i):
                sieve[j] = False

    return primes


