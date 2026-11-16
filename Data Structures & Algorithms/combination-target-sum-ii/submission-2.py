class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(start, temp, total):
            if total == target:                 # check the target FIRST
                res.append(temp[:])             # append a COPY
                return

            for i in range(start, len(candidates)):
                # skip duplicates at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # sorted, so if this one's too big, all later ones are too
                if total + candidates[i] > target:
                    break

                temp.append(candidates[i])                       # choose
                backtrack(i + 1, temp, total + candidates[i])    # i + 1: use each number once
                temp.pop()                                       # un-choose (backtrack)

        backtrack(0, [], 0)
        return res