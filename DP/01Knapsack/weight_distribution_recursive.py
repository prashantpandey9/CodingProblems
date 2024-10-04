"""
Input: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
Output: 3
Explanation: There are two items which have weight less than or equal to 4. If we select the item with weight 4, the possible profit is 1. And if we select the item with weight 1, the possible profit is 3. So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.


Input: N = 3, W = 3, profit[] = {1, 2, 3}, weight[] = {4, 5, 6}
Output: 0
"""

def knapsack(wt, n, profit, weight):
    if (wt == 0 or n == 0):
        return 0

    if (weight[n-1] > wt):
        return knapsack(wt, n-1, profit, weight)

    else:
        return max(profit[n-1] + knapsack(wt-weight[n-1], n-1, profit, weight), knapsack(wt, n-1, profit, weight))


if __name__ == "__main__":
    profit = [600, 100, 120]
    weight = [10, 20, 30]
    wt = 50
    n = 3
    print(knapsack(wt, n, profit, weight))