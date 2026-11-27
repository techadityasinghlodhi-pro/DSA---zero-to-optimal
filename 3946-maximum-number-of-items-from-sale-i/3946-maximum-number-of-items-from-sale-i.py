class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for _, price in items)

        # Copies gained when buying item i for the first time:
        # 1 bought copy + 1 free copy for each j != i where items[i][0] divides items[j][0]
        gain = [0] * n
        for i, (n, _) in enumerate(items):
            freebies = sum(
                1 for j, (m, _) in enumerate(items) if i != j and m % n == 0
            )
            gain[i] = 1 + freebies

        dp = [0] * (budget + 1)
        for (i, price), g in zip(items, gain):
            for s in range(budget, price - 1, -1):
                if dp[s - price] + g > dp[s]:
                    dp[s] = dp[s - price] + g

        ans = 0
        for s in range(budget + 1):
            extra = (budget - s) // min_price
            ans = max(ans, dp[s] + extra)

        return ans