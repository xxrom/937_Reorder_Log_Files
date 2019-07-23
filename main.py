import re


class Solution(object):
    def reorderLogFiles(self, logs):
        wordLog = []
        digitLog = []

        for logRaw in logs:
            log = logRaw.split()
            isDigitLog = re.search('^(\d+)', log[1]) is not None
            if isDigitLog:
                digitLog.append(' '.join(log))
            else:
                wordLog.append([log[0], ' '.join(log[1:])])

        wordLog.sort(key=lambda item: item[0])
        wordLog.sort(key=lambda item: item[1])

        print(wordLog)

        # i = 0
        # startIndex = None
        # subSort = []
        # while i < len(wordLog) - 1:
        #     if (
        #         (i < len(wordLog) - 1 and wordLog[i][1] == wordLog[i + 1][1])
        #         or (i > 0 and wordLog[i - 1][1] == wordLog[i][1])
        #     ):
        #         if startIndex is None:
        #             startIndex = i
        #     elif len(subSort) > 0:
        #         # todo subsort
        #         sub = wordLog[startIndex:i]
        #         sub.sort(key=lambda item: item[0])

        #         print('wordLog b', wordLog)
        #         g = [item for innerIndex, item in enumerate(
        #             wordLog) if innerIndex < startIndex and innerIndex >= i]

        #         print('wordLog a', g)
        #         subSort = []
        #         startIndex = None
        #     else:
        #         print('empty')
        #     i += 1

        ans = [" ".join(item) for item in wordLog]
        ans.extend(digitLog)
        print('ans',  ans)
        return ans


sol = Solution()

log0 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7",
        "ab1 off key dog", "a8 act zoo", "a2 act car"]
sol.reorderLogFiles(log0)
