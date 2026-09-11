class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        seen = {}
        res = len(words)
        for i, word in enumerate(words):
            for char in word:
                if char not in allowed:
                    res -= 1
                    break
        return res

