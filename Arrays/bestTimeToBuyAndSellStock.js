/*
Source:https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Question:You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in 
the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Solution:
Initilize maxprofit and minimum price so far.Loop through the array 
calculate mimimum so far bu comparing the current element and minimum so far
calculate currentprofit as currentelement - minimum so far
calculate maxprofit comparint currentprofint and max profit
return maxprofit
*/

var maxProfit = function(prices) {
    let maxprofit = 0
    let minimumsofar = prices[0]
    for (i=0; i<prices.length; i++){
        
        minimumsofar = Math.min(minimumsofar, prices[i])
        let currentprofit = prices[i] - minimumsofar
        maxprofit = Math.max(maxprofit, currentprofit)
    }
    return maxprofit
};