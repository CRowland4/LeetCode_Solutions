"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104"""

"""First solution is to keep track of the minimum stock and the maximum profit. Start at the first element in the list
and 0, respectively. For each element in the list, the minimum_stock variable is reassigned to be the minimum of the
current minimum_stock and the current element of the list. The maximum profit is then reassigned to be the maximum
of the current maximum_stock, and the difference between the current price and the current minimum_stock."""


def maxProfit(prices: list) -> int:
    min_stock = prices[0]
    max_profit = 0

    for price in prices:
        min_stock = min(min_stock, price)
        max_profit = max(max_profit, price - min_stock)

    return max_profit


# After looking
"""Just different variations of the same algorithm."""
