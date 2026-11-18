class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for curr in strs:
            temp = [0] * 26
            for c in curr:
                temp[ord(c) - ord('a')] += 1
            key = tuple(temp)
            if key in seen:
                seen[key].append(curr)
            else:
                seen[key] = [curr]
        return list(seen.values())