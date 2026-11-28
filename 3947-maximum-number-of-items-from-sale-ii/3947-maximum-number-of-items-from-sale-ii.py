from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cnt = [0] * (n + 1)
        min_price = float('inf')

        for factor, price in items:
            cnt[factor] += 1
            if price < min_price:
                min_price = price

        # mult_cnt[f] = total items whose factor is a multiple of f
        mult_cnt = [0] * (n + 1)
        for f in range(1, n + 1):
            if cnt[f] > 0:
                for m in range(f, n + 1, f):
                    mult_cnt[f] += cnt[m]

        # Build (price, max_2_item_copies) for items cheaper than 2 * min_price
        bundles = []
        for factor, price in items:
            cap = mult_cnt[factor] - 1
            if cap > 0 and price < 2 * min_price:
                bundles.append((price, cap))

        bundles.sort()

        total_items = 0
        for price, cap in bundles:
            if budget < price:
                break
            take = min(cap, budget // price)
            total_items += take * 2
            budget -= take * price

        # Spend remaining budget on the cheapest item (1 item per copy)
        total_items += budget // min_price

        return total_items