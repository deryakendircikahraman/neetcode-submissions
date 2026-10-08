class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqList=set()
        for num in nums:
            if num in uniqList:
                return True
            else:
                uniqList.add(num)
        return False
           
            
        