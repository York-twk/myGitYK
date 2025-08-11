
def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans = []
        for x in candies:
            new_candy = x + extraCandies
            if(new_candy >= max(candies)):
                ans.append(True)
            else:
                ans.append(False)        
        return ans


ori_candies = [2,3,5,1,3]
ori_ex_candies = 3
print(kidsWithCandies("", ori_candies, ori_ex_candies))