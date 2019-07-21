import re


class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        print(logs)

        split = []
        wordLog = []
        digitLog = []

        for logRaw in logs:
            log = logRaw.split()
            isDigitLog = re.search('^(\d+)', log[1]) is not None
            print('log', log[1], isDigitLog)
            if isDigitLog:
                digitLog.append(' '.join(log))
            else:
                wordLog.append([log[0], ' '.join(log[1:])])

        print('digitLog', digitLog)
        print('wordLog', wordLog)


sol = Solution()

log0 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
sol.reorderLogFiles(log0)
