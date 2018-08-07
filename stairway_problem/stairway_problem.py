import time

def s_recursion(steps, strides, cache=[1]):
    count = 0
    for stride in strides:
        count += cache[len(cache) - stride] if len(cache) - stride >= 0 else 0
    cache.append(count)
    if len(cache) - 1 == steps:
        total = cache[len(cache) - 1]
        del cache[1:]
        return total
    return s_recursion(steps, strides, cache)

def s_cached(n, X):
    cache = [0] * (n + 1)
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]

def compare(steps, strides):
    time_start = time.clock()
    cache_value = s_cached(steps, strides)
    time_total = (time.clock() - time_start) * 1000
    # print(f"Cache method - Combos: {cache_value} Time: {time_total:.6}")
    time_start = time.clock()
    recursion_value = s_recursion(steps, strides)
    time_total2 = (time.clock() - time_start) * 1000
    # print(f"Recursion - Combos: {recursion_value} Time: {time_total2:.6}")
    return 'cache' if time_total < time_total2 else 'recursion'

steps = 4
x = {x for x in range(1, 6, 2)}
y = [1, 2]

winners = {'cache': 0, 'recursion': 0}

time_start = time.clock()
for _ in range(100):
    winners[compare(5, x)] += 1
time_total = time.clock() - time_start

print(f'{winners}\n{time_total:.6}')