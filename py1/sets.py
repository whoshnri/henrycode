#sets are mutables and cannot contain duplicate elemets
#initialised with curly brackets
myset = {1,2,3,2,4,5,6,7,8,9}
myset2 = {"Henry" , "Moshood", "Collins"}
print(myset2)

#it can also be declared usig the "set" command then paratheses () followed by a list of items
myset1 = set(["hello", "nancy" , "lauren"])
print(myset1)

#sets are useful for storing individual characters of strings..although the order of storage is arbitrary
myset3 = set("Henry")
print(myset3)

#empty set
myset4 =set()
print(type(myset4))

#adding elements to myset4
myset4 = set("Henry")#this adds the characters as items
myset4.add(1)
print(myset4)
myset4.remove(1) #removes 1
print(myset4)
#removing existing items in a set with .discard
myset4.discard("e")#also works as remover
print(myset4)

#pop can be used but since its not an ordered list it will retur an arbitrary last item
for i in myset4:
    print(i)

myset4.add("e")
if 'e' in myset4:
        print("e exists")
else:
    print("e is absent")


#union and intersection of sets
odd = set([1,3,5,7,9])
even = {0,2,4,6,8}
prime = {2,3,5,7}
print(type(odd))

#union
u = odd.union(even)
print(u)
intersection = even.intersection(odd)
print(intersection) #return an empty set

#difference of a set
#are elements in set a that are absent in set b
diff = odd.difference(prime)
print(diff)#returns odd numbers that are not prime numbers

#symmetric difference
#returns all elements besides elements that appear in both sets
diff2 = odd.symmetric_difference(prime)
print(diff2)#cool

#updating a set with another set without duplication using the .update command
myset.update(myset1)
print(myset)

#the .intersection_update command updates the values of set a using the values found in sets a and b
#no examples on the for now please
#its quite basic to understand by now
#likewise the symmetric_intersection_update updates set a with the values found in sets a and b except the intersections

#subsets and superset
#for set b to be a subset of a, all the items in set b must be found in set a
#for set A too be a superset of B then B must be a subset of A
setA =set([0,1,2,3,4,5,6,7,8])
setB = {0,1,2,3,4}
setC = set("Adeshayo")
print(setC)
print(setB.issubset(setA))
print(setA.issuperset(setB))

#is two sets a and b are disjointed it means that they share no similar values
setsA = {1,2,3,4}
setsB = set([5,6,7,8,9])
if setsA.isdisjoint(setsB) :#true since they have no silimar values
    print("they are disjointed")
else:
     print("they have some similar values")


#as we did with lists and tuples, copying a set is dont using the .copy() or set(setX) methods
copyA = set([1,2,3,4,5,6,7,8,9])
copyB = set(copyA)
copyC = copyB.copy()

print(copyA)
print(copyB)
print(copyC)

#frozen set---is a way to make a set immutable
frozen = frozenset([1,2,3,4,5,6,7,8,9])
print(frozen)




