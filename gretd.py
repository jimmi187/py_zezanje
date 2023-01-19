

print() # [8, 10]
from functools import wraps
from time import time

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		start_time = time()
		result = fn(*args, **kwargs)
		end_time = time()
		print(f"Executing {fn.__name__}")
		print(f"Time Elapsed: {end_time - start_time}")
		return result
	return wrapper


def two_oldest_ages():
    lista= [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
    c=0
    for x in range(len(lista)):
        c += lista[x][x] + lista[-1-x][x] 
    return c


def two_oldest_ages2():
    arr= [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
    total = 0
    
    for i,val in enumerate(arr):
        total += arr[i][i]
        total += arr[i][-1-i]
    return total



if __name__ == '__main__':
    import timeit
    
    print(timeit.timeit("two_oldest_ages()", setup="from __main__ import two_oldest_ages"))
    
    
    print(timeit.timeit("two_oldest_ages2()", setup="from __main__ import two_oldest_ages2"))
