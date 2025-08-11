import LOG
import json


print('start')

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    col_len = len(matrix[0])
    p1, p2 = 0, len(matrix) * len(matrix[0]) - 1
    
    while p1 <= p2:

        mid = int((p1 + p2) / 2)

        mid_matrix = matrix[mid // col_len][mid % col_len]
        if  mid_matrix== target:
            return True
        elif mid_matrix < target:
            p1 = mid + 1
        elif mid_matrix > target:
            p2 = mid - 1
    
    return False



input = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
number = 3

print(searchMatrix(matrix = input, target = number))

        



