class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def dayOfYear(date):
            month = int(date[:2])
            day = int(date[3:])

            total = day
            for i in range(month - 1):
                total += days[i]

            return total

        a1 = dayOfYear(arriveAlice)
        a2 = dayOfYear(leaveAlice)
        b1 = dayOfYear(arriveBob)
        b2 = dayOfYear(leaveBob)

        start = max(a1, b1)
        end = min(a2, b2)

        return max(0, end - start + 1)

        