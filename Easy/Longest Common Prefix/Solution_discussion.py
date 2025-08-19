# An interesting problem
# checking iteratively has lesser time complexity but the solution for some reason isn't faster.
# Sorting the entire list and comparing the first and last string is sufficient to find the common prefix although this has higher complexity this is a super fast approach compared to the former

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        t = ""
        for i in range(len(strs[0])):
            if strs[0][i]!=strs[-1][i]:
                return t
            t+=strs[0][i]

        return t
