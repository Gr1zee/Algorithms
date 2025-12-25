class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_len = len(strs[0])
        if len(strs) == 1:
            return strs[0]
        for i in range(1, len(strs)):
            min_len = min(min_len, len(strs[i]))
        for i in range(min_len):
            b = strs[0][i]
            for word in strs[1:]:
                if word[i] != b:
                    return res
            res += b
        return res
