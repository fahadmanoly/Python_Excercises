# generating n prime numbers

def generate_prime_numbers(n):
    prime_numbers = [2,3]
    if n <1:
        return
    if n == 1:
        prime_numbers.pop()
        return prime_numbers
    if n == 2:
        return prime_numbers
    if n > 2:
        p=prime_numbers[-1] + 2
        while len(prime_numbers) < n:
            d=2
            while d <= p//2:
                if p%d == 0:
                    p = p + 2
                    break
                else:
                    d=d+1
            else:
                prime_numbers.append(p)
                p = p + 2
        return prime_numbers
                       
prime_nos_list = generate_prime_numbers(10)
print(prime_nos_list)
                