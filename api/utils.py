import requests

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 1:
        return False
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    num_str = str(abs(n))
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

def digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        if response.status_code == 200:
            return response.text
        else:
            return "No fun fact available."
    except requests.RequestException:
        return "Error fetching fun fact."
