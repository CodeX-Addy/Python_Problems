#  By using lambda and reduce method
from functools import reduce

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1]
print(fib(5))
                       
# By using lambda and map function
def fibonacci(count):
	fib_list = [0, 1]

	any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
										range(2, count)))

	return fib_list[:count]

print(fibonacci(10))

