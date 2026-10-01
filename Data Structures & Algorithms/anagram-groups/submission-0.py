class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []

        # lookup store the pattern and its words
        lookup = defaultdict(list)
        for s in strs:
            pattern = [0] * 26
            for c in s:
                pattern[ord(c) - ord('a')] += 1
            lookup[tuple(pattern)].append(s)
        
        return list(lookup.values())
