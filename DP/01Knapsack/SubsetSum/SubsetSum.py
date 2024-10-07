"""
Subset Sum Problem
Given a set of non-negative integers and a value sum, the task is to check if there is a
subset of the given set whose sum is equal to the given sum. 

Examples: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
Explanation: There is a subset (4, 5) with sum 9.


Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
Explanation: There is no subset that add up to 30.
"""





dp = [[]]
def subset_sum(arr, s, dp):
    n = len(arr)
    # Fill the subset table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            if j >= arr[i-1]:
                dp[i][j] = (dp[i-1][j] or
                                dp[i - 1][j-arr[i-1]])


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    s = 9
    n = len(arr)
    
    # initialize matrix
    t = [[-1]*(s+1)] * (n+1)
    for i in range(n+1):
        for j in range(s+1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True
    
    subset_sum(arr, s, t)
    print(t[n][s])