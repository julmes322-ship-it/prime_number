import math

def get_factorization(n):
    """소인수분해를 수행하여 리스트로 반환 (반복적 나눗셈 방식) [cite: 6]"""
    factors = []
    temp = n
    d = 2
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors

def check_prime_with_details(n):
    """소수 여부를 판별하고, 소수가 아니라면 구성 숫자를 출력"""
    if n < 2:
        return f"{n}은(는) 소수가 아니며, 1보다 큰 자연수가 아닙니다."
    
    # √n까지 나눗셈을 수행하여 최적화 [cite: 1, 5]
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        return f"✅ {n}은(는) 소수입니다."
    else:
        # 소수가 아닐 경우 어떤 수(소인수)로 이루어져 있는지 계산 [cite: 2, 6]
        factors = get_factorization(n)
        factors_str = " × ".join(map(str, factors))
        return f"❌ {n}은(는) 소수가 아닙니다.\n   구성 성분(소인수분해): {factors_str}"

def get_primes_by_sieve(limit):
    """에라토스테네스의 체를 이용한 다수 소수 생성 [cite: 6]"""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_p in enumerate(sieve) if is_p]

def main():
    while True:
        print("\n" + "="*30)
        print(" [2026 DEV-ON] 소수 관리 프로그램")
        print("="*30)
        print("1. 소수 판별 및 구성 확인")
        print("2. 특정 범위 소수 생성")
        print("3. 소인수분해 상세 수행")
        print("4. 종료")
        
        choice = input("원하는 메뉴 번호: ")

        if choice == '1':
            num = int(input("확인할 숫자를 입력하세요: "))
            print(check_prime_with_details(num))

        elif choice == '2':
            limit = int(input("어디까지 소수를 생성할까요?: "))
            primes = get_primes_by_sieve(limit)
            print(f"결과: {primes}")
            print(f"총 {len(primes)}개의 소수가 발견되었습니다.")

        elif choice == '3':
            num = int(input("소인수분해할 숫자를 입력하세요: "))
            if num < 2:
                print("2 이상의 자연수를 입력하세요.")
            else:
                factors = get_factorization(num)
                print(f"결과: {' × '.join(map(str, factors))}")

        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()