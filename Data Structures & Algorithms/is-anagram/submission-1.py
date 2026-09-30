# using 2 hashmap to store the pattern of s and t
# then compare it to see if they are anagrams of each other

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        elif not s:
            return False
        elif not t: 
            return False
        
        lookup_s = defaultdict(int)
        lookup_t = defaultdict(int)

        for c in s:
            lookup_s[c] += 1
        for c in t:
            lookup_t[c] += 1
        
        if lookup_s == lookup_t:
            return True
        else:
            return False
