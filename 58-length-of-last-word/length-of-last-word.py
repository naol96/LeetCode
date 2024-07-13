class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        alpha=s.split()
        n=len(alpha)-1
        return len(alpha[n])