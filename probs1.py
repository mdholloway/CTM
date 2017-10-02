# 1.7.1
def my_filter(L, num): return [n for n in L if n % num != 0]

# 1.7.2
def my_lists(L): return [[n for n in range(1, int + 1)] for int in L]

# 1.7.3
def my_function_composition(f, g):
    result = {}
    for key in f:
        x = f[key]
        result[key] = g[x]
    return result

# 1.7.4
def mySum(L):
    current = 0
    for x in L:
        current = current + x
    return current

# 1.7.5
def myProduct(L):
    current = 1
    for x in L:
        current = current * x
    return current

# 1.7.6
def myMin(L):
    current = sys.maxsize
    for x in L:
        current = x if x < current else current
    return current

# 1.7.7
def myConcat(L):
    current = ''
    for x in L:
        current = current + x
    return current

# 1.7.8
def myUnion(L):
    current = set()
    for x in L:
        for n in x:
            if n not in current:
                current.add(n)
    return current

# 1.7.9
1) 0
2) 1
3) the max integer
4) ''
5) an empty set

# 1.7.10
a) 5 + 3i
b) i
c) -1 + .001i
d) .001 + 9i

# 1.7.11
a) e^3i
b) e^(11π/12)i
c) e^(5π/12)i

# 1.7.12
def transform(a, b, L):
    result = []
    for n in L:
        result.append(a * n + b)
    return result

a) a = -2i-2i^2, b = 1+i
b) a = 1+1.5i, b = -3-2i

# 1.7.13
a) 1
b) 0
3) 0

        
