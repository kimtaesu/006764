def runtime(f):
    def wrapper():
        import timeit
        start = timeit.default_timer()
        f
        end = timeit.default_timer()
        print(end - start)
        return f()

    return wrapper


@runtime
def odd_sum_for():
    result = 0
    n = 1000000000000

    for i in range(0, n + 1):
        if n > 1000:
            return "1000과 같거나 작은 수를 입력하세요!"
        elif not i % 2 == 0:
            result += i
    return "1부터 {n}까지 홀수의 합 : {result}".format(n=n, result=result)


odd_sum_for()
