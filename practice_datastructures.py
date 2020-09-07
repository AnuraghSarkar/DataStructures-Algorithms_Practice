# def compare(value1, value2):
#     """
#     Function to compare two string int values without converting through int. O(n^2)
#     """
#     if len(value1) > len(value2):
#         print(f'{value1} is greater than {value2}')
#     elif len(value1) < len(value2):
#         print(f'{value2} is greater than {value1}')
#     elif value1 == value2:
#         print(False)
#     elif len(value1) == len(value2):
#         for i in range(len(value1)):
#             if value1[i] == value2[i]:
#                 continue
#             elif value1[i] > value2[i]:
#                 print(f'{value1} is greater than {value2}')
#             else:
#                 print(f'{value2} is greater than {value1}')
#                 return
#
#
# compare('1111', '1112')
#
# def dia(D2_list):
#     """
#     Function to add the diagonal element of 2-D list. O(n)
#     """
#     total = 0
#     for i in range(len(D2_list)):
#         total += D2_list[i][i]
#     print(total)
#
#
# dia([[5, 4, 2],
#      [4, 8, 5],
#      [7, 2, 3]])
# def diagonalDifference(arr):
#     """
#     Function to find |list|. O(n)
#     """
#     left = 0
#     right = 0
#     for i in range(len(arr)):
#         left += arr[i][i]
#         right += arr[i][len(arr) - 1 - i]
#     return abs(left - right)
#
#
# print(diagonalDifference([[6,8], [-6,9]]))

#
# def rookie_crasher(chess):
#     """
#     Function to check a 2-D array list that represent a chess board, check if one rookie can attack other rookie or not.
#     """ O(n^2)
#     for row_i in range(len(chess)):
#         row = 0
#         for j in range(len(chess[row_i])):
#             row += chess[row_i][j]
#         if row > 1:
#             print('Rookie Crasher!')
#             return
#
#     for col_i in range(len(chess)):
#         col = 0
#         for j in range(len(chess[col_i])):
#             col += chess[j][col_i]
#         if col > 1:
#             print('Rookie Crasher!')
#             return
#     else:
#         print('Rookie is safe!')
#         return
#
#
# rookie_crasher([[1, 0, 1, 0],
#                 [0, 1, 0, 0],
#                 [0, 0, 0, 1],
#                 [0, 0, 0, 0]])
#
#
# def count_negative(D2):
#     """
#     Function to check how many negative number are there in 2-D list with minimum time complexity as possible. O(n)
#     """
#     count = 0
#     row = 0
#     col = len(D2[0] -1)
#     while col >0 and row < len(D2):
#         if D2[row][col] <0:
#             count += (col+1)
#             row += 1
#         else:
#             col -= 1
#     print(count)
#     return
#
#
# count_negative([[-4, -3, -1, 1],
#                 [-2, -2, 1, 2],
#                 [-1, 1, 2, 3],
#                 [1, 2, 4, 5]])
#
#

# def sum_10_dict(dic):
#     """
#     Function to print the sum of 10 pairs from list in a dict if not then ad. Time complexity is O(n).
#     """
#     a = {}
#     for i in dic:
#         if (10 - i) in a:
#             return print(f'{10 - i},{i}')
#         a[i] = 1
#
#     print('No valid pair in dict.')
#
#
# sum_10_dict([3, 4, 1, 2, 9])


