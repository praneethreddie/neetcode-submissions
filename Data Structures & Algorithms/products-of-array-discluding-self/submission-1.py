class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total=1
        zero_count=nums.count(0)

        for i in nums:
            if i!=0:
                total*=i

        res=[]
        for i in nums:
            if zero_count>1:
                res.append(0)
            elif zero_count==1:
                if i==0:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(total//i)
        return res