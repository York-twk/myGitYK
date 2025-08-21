

def findMaxAverage(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    """
    使用滑動窗格，比較總和
    滑動出閣只需扣掉第一位置的值，再加上下一個末位置的值，不須陣列重新加總
    """
    max_sum = sum(nums[:k])
    n_sum = max_sum
    for i in range(k, len(nums)):       
        n_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, n_sum)

    return float(max_sum)/k


arr = [1,12,-5,-6,50,3]
kk = 4
print("ans: ", findMaxAverage("", arr, kk))