#creating the list to search through

binary_list = []
for i in range(1000):
    binary_list.append(i)


def find(x):
    p = len(binary_list)
    found = False
    while found == False:
        if p % 2 != 0 :
            p = p + 1
        p = p / 2
        find = binary_list[int(p)]
        if find == x :
            print(f'The number {x} found at index {int(p)}')
            found = True
        
find(123)



