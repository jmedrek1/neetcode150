class Solution(object):
    def isAnagram(self, s, t):
        for letter in s:
            if letter in t:
                t = t.replace(letter, '', 1)
            else:
                return False
        return t == ''