def cache_decorator(function):
    mem_cache = {}
        
    def cached_fucntion(argument):
        if argument in mem_cache:
            return mem_cache[argument]
        else:
            mem_cache[argument] = function(argument)
            return mem_cache[argument]
    
    return cached_fucntion

@cache_decorator
def fib(n):
    if (n == 0) or (n == 1):
        return n
    return fib(n-1)+fib(n-2)
