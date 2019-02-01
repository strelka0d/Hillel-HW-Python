import collections
import functools

# LRU (least recently used) — это алгоритм, при котором вытесняются значения, которые дольше всего не запрашивались.
# Соответственно, необходимо хранить время последнего запроса к значению. И как только число закэшированных значений
# превосходит N необходимо вытеснить из кеша значение, которое дольше всего не запрашивалось.
#
#
# Задача - 1
# Создать декоратор lru_cache(подобный тому который реализован в Python).
#
# Задача-2
# Ваш lru_cache декоратор должен иметь служебный метод
# cache_info  - статистика использования вашего кеша(например: сколько раз вычислялась ваша функция,
# а сколько раз значение было взято из кеша, сколько места свободно в кеше)
#
# Задача-3
# Ваш lru_cache декоратор должен иметь служебный метод
# cache_clear - очищает кеш
#
# Пример обращения к служебному методу декоратора


def lru_cache(max_size=3):
    """Least-recently-used cache decorator"""

    def decorating_func(func):
        cache = collections.OrderedDict()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = args

            # def key_constract(args, kwargs):
            #     key = args
            #     if kwargs:
            #         key += tuple(sorted(kwargs.items()))
            #     return key
            #
            # key = key_constract(args, kwargs)

            try:
                res = cache.pop(key)
                wrapper.hits += 1
            except KeyError:
                res = func(*args, **kwargs)
                wrapper.misses += 1

                if len(cache) >= max_size:
                    cache.popitem()

            cache[key] = res

            return res


        def cache_info():
            """ LRU cache statistic"""
            free_space = max_size - len(cache)
            print({"cache": dict(cache),
                   "hits": wrapper.hits,
                   "misses": wrapper.misses,
                   "free space": free_space
                    })

        def cache_clear():
            """Clear the cash and the cache statistics"""
            cache.clear()
            wrapper.hits = wrapper.misses = 0

        wrapper.hits = wrapper.misses = 0
        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear

        return wrapper

    return decorating_func


@lru_cache()
def my_func(x, y):
    return x * y


my_func(1, 2)
my_func(6, 4)
my_func(5, 8)
my_func(6, 4)

my_func.cache_info()
my_func.cache_clear()