from random import randint
import time

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                # buff = array[j+1]
                # array[j] = array[j + 1]
                # array[j+1] = buff


def selection_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]


def insertion_sort(array):
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key



def Quick_Sort(array):
    def Partition(array, start, end):
        pivot = array[(start + end) // 2]
        i = start - 1
        j = end + 1
        while True:
            i += 1
            while array[i] < pivot:
                i += 1
            j -= 1
            while array[j] > pivot:
                j -= 1
            if i >= j:
                return j
            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            array[i], array[j] = array[j], array[i]

    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _Quick_Sort(items, start, end):
        if start < end:
            split_index = Partition(items, start, end)
            _Quick_Sort(items, start, split_index)
            _Quick_Sort(items, split_index + 1, end)

    _Quick_Sort(array, 0, len(array) - 1)



def heap_sort(nums):
    def heapify(nums, heap_size, root_index):
        # Индекс наибольшего элемента считаем корневым индексом
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        # Если левый потомок корня — допустимый индекс, а элемент больше,
        # чем текущий наибольший, обновляем наибольший элемент
        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        # То же самое для правого потомка корня
        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child

        # Если наибольший элемент больше не корневой, они меняются местами
        if largest != root_index:
            nums[root_index], nums[largest] = nums[largest], nums[root_index]
            # Heapify the new root element to ensure it's the largest
            heapify(nums, heap_size, largest)

    n = len(nums)

    # Создаём Max Heap из списка
    # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)








N = 1000000
a = []
for i in range(N):
    a.append((randint(1, 99)))

# print(a)
# start = time.time()
# bubble_sort(a)                # Пузырьком
# end = time.time() - start
# print('bubble_sort', end)
# print(a)


# start = time.time()
# selection_sort(a)             # Выбором
# end = time.time() - start
# print('selection_sort', end)
# # print(a)
# time.sleep(10)


# start = time.time()
# insertion_sort(a)             # Вставкой
# end = time.time() - start
# print('insertion_sort', end)
# print(a)


# start = time.time()
# Quick_Sort(a)                   # Быстрая сортировка
# end = time.time() - start
# print(a)
# print('Quick_Sort', end)


# start = time.time()
# heap_sort(a)                   # Пирамидальная сортировка (кучей)
# end = time.time() - start
# print(a)
# print('heap_sort', end)





