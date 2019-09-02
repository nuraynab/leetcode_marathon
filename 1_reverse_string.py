class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n == 1 or n == 0:
            s
        else:
            for i in range (int(n/2)):
                s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
