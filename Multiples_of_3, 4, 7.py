"""
If we list all positive integers below 10 that are multiples of 3, 4, or 7 we get: [3, 4, 6, 7, 8, 9]. The sum of the list is 37.

Given a positive integer n, return the sum of all numbers less than or equal to n that are multiples of 3, 4, or 7.

Example 1
Input

n = 7
Output

20
Explanation

The solution includes [3, 4, 6, 7] and its sum is 20.

"""

class Solution:
    def solve(self, n):
        # Write your code here
        sum = 0
        for i in range(n+1) :
            if (i % 3 == 0) or (i % 4 == 0) or (i % 7 == 0):
                sum += i
                
        return sum