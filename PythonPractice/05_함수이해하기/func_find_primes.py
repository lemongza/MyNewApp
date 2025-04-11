# 시작값, 끝값을 인자로 받아 그 사이의 소수를 리스트로 반환하는 find_primes 함수를 작성하세요.

def find_primes(n1, n2):
    primes = []
    for num in range(n1, n2 + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i != 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    print(primes)

find_primes(1, 30)


            