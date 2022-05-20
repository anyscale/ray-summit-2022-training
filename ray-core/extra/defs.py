import multiprocessing as mp


def get_cpu_count():
    return mp.cpu_count()


def is_prime(n):
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return 0
    return 1