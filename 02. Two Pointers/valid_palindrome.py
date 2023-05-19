class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = ''.join(x for x in s if x.isalnum()).lower()

        return st == st[::-1]