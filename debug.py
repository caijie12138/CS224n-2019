import pysnooper
@pysnooper.snoop()
def findDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            while i != nums[i]-1:
                if nums[i] != nums[nums[i]-1]:
                    tmp = nums[i]
                    nums[i] = nums[nums[i]-1]
                    nums[tmp-1] = tmp
                else:
                    res.append(nums[i])
                    break
        return res


if __name__=='__main__':
    findDuplicates([4,3,2,7,8,2,3,1])
