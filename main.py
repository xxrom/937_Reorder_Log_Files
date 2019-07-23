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

        ans = [" ".join(item) for item in wordLog]
        ans.extend(digitLog)
        return ans


sol = Solution()

log0 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7",
        "ab1 off key dog", "a8 act zoo", "a2 act car"]
sol.reorderLogFiles(log0)
