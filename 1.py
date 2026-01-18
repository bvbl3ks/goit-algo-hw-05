def caching_fibonacci():
    da_cache = {}

    def fibonacci(X):
        if X <= 0:
            return 0
        if X == 1:
            return 1
        if X in da_cache:
            return da_cache[X]

        da_cache[X] = fibonacci(X - 1) + fibonacci(X - 2)
        return da_cache[X]

    return fibonacci

fiba = caching_fibonacci()

print(fiba(10)) 
print(fiba(15))  
print(fiba(20))
