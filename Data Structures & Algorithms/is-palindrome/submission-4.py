class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(filter(str.isalnum, s)).lower()
        p2 = len(word) - 1

        for i in range(int(len(word)/2)):
            if word and word[i] != word[p2]:
                return False
            p2 -= 1
        return True
