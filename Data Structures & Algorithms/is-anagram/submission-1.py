class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count1=Counter(s.lower())
        count2=Counter(t.lower())
        if count1==count2:
            return True
        else:
            return False