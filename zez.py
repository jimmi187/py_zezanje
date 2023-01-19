import sys
people = ["jhonu", "mile", "cile", "vile"]
a = all(map(lambda x : isinstance(x,str), people))
b = (isinstance(x,str) for x in people)
c = ([isinstance(x,str) for x in people])

# print(c)
# print(sys.getsizeof(a))
# print(sys.getsizeof(c))

nesto = [300, 20, -900]
aa = filter(lambda x : x % 2 ==0, nesto)
bb = ([x for x in nesto if x % 2 ==0])
print(tuple(aa))
print(bb)

print(sys.getsizeof(aa))
print(sys.getsizeof(bb))


def sum_floats(*args):
    return sum((filter(lambda x : isinstance(x,float), args)))


print((sum_floats(1.5, 2.4, 'awesome', [], 1)))


nes = (x for x in range(222220000000000000000000000))
g = tuple("mejl:pass".split(":"))
s = tuple("stavrno@gmail.com:nesotasfasf".split(":"))
s1 = tuple("stavrno@gmail.com1:nesotasfasf".split(":"))
s2 = tuple("stavrno@gmail.com2:nesotasfasf".split(":"))
s3 = tuple("stavrno@gmail.com3:nesotasfasf".split(":"))
l = [s3,s1,s2,s]
lista_recnika = [ dict(zip(g,x)) for x in l]
# print(lista_recnika)
# print(sorted(lista_recnika, key=lambda x : x['mejl']))


midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

recnik = dict(zip(
                students, 
                map(lambda x: max(x), 
                    zip(midterms, finals))
                ))

print(recnik)


def interleave(x , y):
    return "".join(i+j for i,j in zip(x,y))

def interleave2(x , y):
    return "".join(map(lambda k: k[0]+k[1], zip(x,y)))

    
interleave2('hi',"ha")

def triple_and_filter(nesto):
    return list(map(lambda x: x*3,(filter(lambda x: x%4==0,nesto))))


#print(list(range(1,len(nes)+1,2)))
import timeit

c = (map(lambda x: x[1],filter(lambda x: x[0]%2==0, enumerate(nes))))

c1 = (y for x,y in enumerate(nes) if x%2==0)






s = "awwwsomeee"
def vowel_count(s):
    print({x :s.count(x) for x in s})

vowel_count(s)
import random

def bingo():
    count = 0
    izvuceni = set()
    while len(izvuceni) < 77:
        count += 1
        next = random.randint(1,78)
        if next not in izvuceni:
            izvuceni.add(next)
            print(next)

    print(f"ovo je broj u while {count}")
    return izvuceni
    


print(sorted(bingo()))


st = "nesto je napisano"
def cap(st):
    print(" ".join((map(lambda x : x[0].upper() + x[1:] , st.split(" ")))))
     

cap(st)


class Card:
    def __init__(self, suit, value):
        self.suit=suit
        self.value=value
    
    def __repr__(self) -> str:
        return("{} of {}".format(self.value,self.suit))


suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

lis = sum(list(map(lambda x: list(map(lambda y: Card(x, y),values)),suits)),[])

print(lis)


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


@speed_test
def g1():
    
    nes = (x for x in range(20000000))   
    return tuple(map(lambda x: x[1],filter(lambda x: x[0]%2==0, enumerate(nes))))
    
@speed_test
def g2():
    
    nes = (x for x in range(20000000)) 
    return tuple(y for x,y in enumerate(nes) if x%2==0)
    
def get_multiples(num=1, count=10):
    for i in range(num, num*(count+1), num):
        print(i)

def find_the_duplicate(l):
    #d = { x : l.count(x) for x in l}
    #d = list(x for x,y in d.items() if y ==2)
    d = list(map(lambda x : x[0] , filter(lambda y: y[1]==2, {x : l.count(x) for x in l}.items())))
    
    print(d)

find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None

k = []
k = sum(k , 0)
'''
list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
sum_up_diagonals(list4) # 68
'''
list4 = [
  [ 1, 2],
  [ 3, 4]
]

def sum_up_diagonals(lista):
    return sum( lista[x][x] + lista[len(lista)-x-1][x] for x in range(len(lista)))

def sum_up_diagonals3(lista):
    return sum(lista[x][x] + lista[-1-x][x] for x in range(len(lista)))

def sum_up_diagonals2(arr):
    for i,val in enumerate(arr):
        print("this is i - > " + str(i))
        print("this is val -> " + str(val))

print(len(list4))
print(sum_up_diagonals(list4))
sum_up_diagonals2(list4)


def find_greater_numbers2(lista):
    c = 0
    #l = list(1 for x in lista[:-1] if x < lista[x+1])

    for x in lista[:-1]:
        print(l)

find_greater_numbers2([6,1,2,7])

def reverse_vowels(st):
    indexi = []
    vrednosti = []
    for i in enumerate(st):
        if i[1] in ('a','e','i','o','u','A','E','I','O','U'):
            indexi.append(i[0])
            vrednosti.append(i[1])
    st = list(st)
    for i in enumerate(reversed(indexi)):
        st[i[1]] = vrednosti[i[0]] 
        
    return("".join(st))
reverse_vowels("Reverse Vowels In A String")


def three_odd_numbers(ls):
    for i in enumerate(ls):
        if i[0]+2 < len(ls):
            if sum(x for x in ls[i[0]:i[0]+3])%2!=0:
                return True
    return False


print(three_odd_numbers([5,2,1]))

def mode(ls):
    k = {x : ls.count(x) for x in ls}
    maximum = max(k)
    for x in k.items():
        if x[1] == maximum:
            return x[0]
        
    

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))

# if __name__ == '__main__':
#     import timeit
    
#     print(timeit.timeit("g1()", setup="from __main__ import g1"))
    
    
#     print(timeit.timeit("g2()", setup="from __main__ import g2"))



