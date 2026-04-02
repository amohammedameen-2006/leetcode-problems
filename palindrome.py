class Solution:
    def isPalindrome(self, x):
        t = x
        r = 0

        if x < 0:
            return False

        while x != 0:
            digit = x % 10
            r = r * 10 + digit
            x = x // 10

        return r == t