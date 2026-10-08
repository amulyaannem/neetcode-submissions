class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=Counter(nums)
        seen=set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False