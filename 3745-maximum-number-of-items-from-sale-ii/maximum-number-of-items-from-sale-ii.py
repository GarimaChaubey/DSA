
class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)

        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        gain = [0] * (n + 1)

        for f in range(1, n + 1):
            for j in range(f, n + 1, f):
                gain[f] += freq[j]

            gain[f] -= 1

        items.sort(key=lambda x: x[1])

        min_price = items[0][1]
        ans = 0

        for factor, price in items:

            if price > 2 * min_price:
                break

            count = gain[factor]

            take = min(count, budget // price)

            ans += take * 2
            budget -= take * price

        ans += budget // min_price

        return ans
