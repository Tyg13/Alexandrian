import multiprocessing
from math import sqrt
__author__ = 'Tyler Lanphear'


def is_alexandrian(n):
    factors = (x for x in range(1, round(sqrt(n / 2)) + 1) if n % x == 0)

    for p in factors:
        try:
            sqrt_of_disc = sqrt((n - p) ** 2 - 4 * n * p ** 3)
            if sqrt_of_disc.is_integer():
                q = int((p - n + sqrt_of_disc) / (2 * p ** 2))
                r = int((p - n - sqrt_of_disc) / (2 * p ** 2))
                if p * q * r == n:
                    print("{}: {}".format(n, (p, q, r)), end="")
                    if n % 6 == 0:
                        print("Div by 6")
                    return True

        except ValueError:
            continue

    return False


def main():
    i = 0
    n = 0

    thread_pool = multiprocessing.Pool(processes=2)

    while True:
        i += 6
        alex_result = thread_pool.apply(is_alexandrian, (i,))

        if alex_result is True:
            n += 1
            print(n)
        if n == 100:
            break


if __name__ == "__main__":
    main()
