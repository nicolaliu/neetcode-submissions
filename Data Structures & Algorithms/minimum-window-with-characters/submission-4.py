# duplicate chars, only one unique answer
# {} to store the chars and their freq in t
# l, r represent the boundary of a sliding window
# s = "OUZODYXAZV", t = "XYZ" need = {x:1, y:1, z:1}
# have = {}
# while have != need: update r
# while have == need: update l, record res and resLen

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        required = Counter(t)
        window = {}
        formed = 0
        needed = len(required)

        best_start = 0
        best_len = float("inf")
        left = 0

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in required and window[ch] == required[ch]:
                formed += 1

            while formed == needed:
                curr_len = right - left + 1
                if curr_len < best_len:
                    best_len = curr_len
                    best_start = left

                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in required and window[left_ch] < required[left_ch]:
                    formed -= 1
                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]

