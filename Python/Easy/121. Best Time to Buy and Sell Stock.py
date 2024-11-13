class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pass

        # Intial Naive Solution
        # # Return 0 if len < 2
        # if len(prices) < 2: return 0
        # # Create initial profit var
        # profit = 0
        # # Create 1st pointer to 1st idx
        # ptr1 = 0
        # # Create 1st while loop while 1st pointer < len - 1
        # while ptr1 < len(prices) - 1:
        #     # Create the 2nd pointer it's 1 > pointer1
        #     ptr2 = ptr1 + 1
        #     # Create 2nd while loop while 2nd pointer < len
        #     while ptr2 < len(prices):
        #         # Subtract the val at pointer 2 from the val at pointer 1, if > profit var
        #         if prices[ptr2] - prices[ptr1] > profit:
        #             # Reassign profit var to the sum
        #             profit = prices[ptr2] - prices[ptr1]
        #         # Add 1 to the 2nd pointer
        #         ptr2 += 1
        #     # Add 1 to the first pointer
        #     ptr1 += 1
        # # Return the profit var
        # return profit