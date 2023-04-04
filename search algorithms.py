from random import randint
import time

def Linear_Search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1


def Binary_Search(array, element):
    first = 0
    last = len(array) - 1
    i = -1
    while (first <= last) and (i == -1):
        mid = (first+last) // 2
        if array[mid] == element:
            i = mid
        else:
            if element < array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return i



N = 1000
a = []
for i in range(N):
    a.append(i)
    i += 1
# print(a)


# start = time.time()
# print(Linear_Search(a, N-1))
# end = time.time() - start
# print('linear_search', ', - time', end)

start = time.time()
print(Binary_Search(a, N-1))
end = time.time() - start
print('linear_search', ', - time', end)
