# 1st task
def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if e >= l[0]]) + [l[0]] + \
               quick_sort([e for e in l[1:] if e < l[0]])


def slice_less(my_list, lesser):
    for i in my_list:
        if i > lesser:
            return quick_sort(my_list)
        else:
            print('Error: element in my_list < lesser')
            break


# print(slice_less([1, 3, 2, 9], 2))
# print(slice_less([6, 3, 2, 8], 1))

# 2nd task

for i in range(11, 80):
    if i % 3 == 0 and i % 5 == 0:
        print('$$@@')
    elif i % 5 == 0:
        print('@@')
    elif i % 3 == 0:
        print('$$')
    else:
        print(i)

