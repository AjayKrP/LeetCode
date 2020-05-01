class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_ = set()
        i = 0
        j = 0
        ans = 0
        while (i < len(s) and j < len(s)): # O(n)
            if not (s[j] in s_):
                s_.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                s_.remove(s[i])
                i += 1
            
        return ans
        
