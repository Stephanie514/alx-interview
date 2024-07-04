def eratosthenes_sieve(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(max_n ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, max_n + 1, start):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    # Calculating max n to know up to where should we calculate primes
    max_n = max(nums)

    # Getting all primes up to the max number in nums using Sieve
    # of Eratosthenes
    primes = eratosthenes_sieve(max_n)

    def simulate_game(n):
        # Creating a set to track remaining numbers
        remaining = set(range(1, n + 1))
        player_turn = 0  # 0 for Maria, 1 for Ben

        while True:
            made_move = False
            for prime in primes:
                if prime in remaining:
                    # Removing prime and its multiples
                    multiples = set(range(prime, n + 1, prime))
                    remaining.difference_update(multiples)
                    made_move = True
                    player_turn = 1 - player_turn
                    break

            if not made_move:
                return "Maria" if player_turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
