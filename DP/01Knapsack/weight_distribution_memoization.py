"""
Input: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
Output: 3
Explanation: There are two items which have weight less than or equal to 4. If we select the item with weight 4, the possible profit is 1. And if we select the item with weight 1, the possible profit is 3. So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.


Input: N = 3, W = 3, profit[] = {1, 2, 3}, weight[] = {4, 5, 6}
Output: 0
"""

def knapsack(n, wt, profit, weight):
    if (n == 0 or wt == 0):
        return 0

    if t[n][wt] != -1:
        return t[n][wt]
    if weight[n-1] > wt:
        t[n][wt] = knapsack(n-1, wt, profit, weight)
        return t[n][wt]
    else:
        t[n][wt] = max(profit[n-1] + knapsack(n-1, wt - weight[n-1], profit, weight), knapsack(n-1, wt, profit, weight))
        return t[n][wt]


if __name__ == "__main__":
    profit = [6, 100, 120]
    weight = [102, 20, 30]
    wt = 50
    n = 3
    
    # initialize matrix
    t = [[-1]*(wt+1)]*(n+1)
    print(knapsack(n, wt, profit, weight))