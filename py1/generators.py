

def mygen():
    yield 1
    yield 2
    yield 3

g = mygen()

#for i in g :
   # print(i)

#for generators , the yield only occurs once
# the next keyword helps to print all the values yielded from a generator in sequence

i = next(g)
print(i) # --> first value
i = next(g)
print(i) # --> next value
i = next(g)
print(i) # --> next value

#another one

def countdown_generator(num):
    print("Starting....: ")
    while num > 0:
        yield num
        num -= 1
n = countdown_generator(5)
print(next(n))
print(next(n))
print(next(n))
print(next(n))


#generators are very memory efficient while working with large data

def first_n(n):
    nums = []
    num = 0
    while num <= n:
        nums.append(num)
        n += 1
    print(nums)

first_n(5)










