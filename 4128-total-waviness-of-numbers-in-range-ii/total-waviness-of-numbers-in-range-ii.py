class Solution(object):
    def totalWaviness(self, num1, num2):

        def solve(x):

            if x <= 0:
                return 0

            s = str(x)
            memo = {}

            def dp(pos, tight, started, prev1, prev2):

                state = (pos, tight, started, prev1, prev2)

                if state in memo:
                    return memo[state]

                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):

                    ntight = tight and (d == limit)

                    if not started and d == 0:

                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            10,
                            10
                        )

                        total_cnt += cnt
                        total_wav += wav

                    elif not started:

                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            d,
                            10
                        )

                        total_cnt += cnt
                        total_wav += wav

                    else:

                        add = 0

                        if prev2 != 10:

                            if prev1 > prev2 and prev1 > d:
                                add = 1

                            elif prev1 < prev2 and prev1 < d:
                                add = 1

                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            d,
                            prev1
                        )

                        total_cnt += cnt
                        total_wav += wav + add * cnt

                memo[state] = (total_cnt, total_wav)
                return memo[state]

            return dp(0, True, False, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)