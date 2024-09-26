def prime_numbers(n: int) -> None:
    primes = [True]*(n+1)
    divisor = 2
    while divisor * divisor <= n:
        if primes[divisor]:
            for i in range(divisor*divisor, n+1, divisor):
                primes[i] = False
        divisor += 1

    print(
        ", ".join(str(i) for i,_ in enumerate(primes[2:], start=2) if primes[i])
    )

prime_numbers(20)
