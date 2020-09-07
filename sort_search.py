# def bubble(array):
#     for i in range(len(array)):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     return array
#
#
# print(bubble([1, 9, 4, 5, 47]))
#
#
# def linear(lists, item):
#     for i in range(len(lists)):
#         if lists[i] == item:
#             return True
#     return False
#
#
# print(linear([1, 2, 3, 4, 5], 4))
#
#
# def quicksort(xs):
#     if xs:
#         import random
#         random.shuffle(xs)
#         below = [i for i in xs[1:] if i < xs[0]]
#         above = [i for i in xs[1:] if i >= xs[0]]
#         return quicksort(below) + [xs[0]] + quicksort(above)
#     else:
#         return xs
#
#
# print(quicksort([465,456,456,45,64,6,456,486]))

#
# def merge(left, right):
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
#
#
# def merge_sort(sort_list):
#     if len(sort_list) == 1:
#         return sort_list
#     middle = len(sort_list) // 2
#     left_data = merge_sort(sort_list[:middle])
#     right_data = merge_sort(sort_list[middle:])
#     return merge(left_data, right_data)
#
#
# data = [100, 5, 200, 3, 100, 4, 8, 9]
# print(merge_sort(data))
#
#
# def binary_search(array, elem):
#     low = 0
#     high = len(array) - 1
#     while low <= high:
#         middle = (low + high) // 2
#         if array[middle] == elem:
#             return True
#         elif array[middle] > elem:
#             high = middle - 1
#         else:
#             low = middle + 1
#     return False
#
#
# print(binary_search(['ram', 'shyam', 'hari'], 'ram'))
#
