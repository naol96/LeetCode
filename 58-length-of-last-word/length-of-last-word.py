class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        alpha=s.split()
        return len(alpha[len(alpha)-1])