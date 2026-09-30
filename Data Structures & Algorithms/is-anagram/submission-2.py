# using 1 hashmap to store the pattern of s first
# then deduct count for chars in t
# then see if all values in hashmap equals 0

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        lookup = defaultdict(int)

        for c in s:
            lookup[c] += 1
        for c in t:
            lookup[c] -= 1
        
        for count in lookup.values():
            if count != 0:
                return False
        
        return True