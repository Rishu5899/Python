# 1 Compute factorial and list primes up to n

# 2 Function to compute factorial iteratively
def factorial(n):
    # 3 handle corner cases
    if n < 0:
        raise ValueError("Negative not allowed")
    # 4 initialize result
    result = 1
    # 5 loop to multiply
    for i in range(2, n + 1):
        result *= i
    # 6 return the factorial
    return result

# 7 Function to check primality
def is_prime(num):
    # 8 not prime if less than 2
    if num < 2:
        return False
    # 9 check divisors up to sqrt(num)
    for j in range(2, int(num**0.5) + 1):
        # 10 found a divisor
        if num % j == 0:
            return False
    # 11 it's prime
    return True

# 12 get input from the user
try:
    n = int(input("Enter a non-negative integer: "))
    # 13 compute and print factorial
    print(f"{n}! =", factorial(n))
    # 14 find primes up to n
    primes = [k for k in range(2, n + 1) if is_prime(k)]
    # 15 print primes
    print("Primes up to", n, ":", primes)
# 16 catch invalid input or errors
except ValueError as e:
    # 17 print error message
    print("Error:", e)
# 18 end of program
# 19 (blank line or comment)
# 20 done
