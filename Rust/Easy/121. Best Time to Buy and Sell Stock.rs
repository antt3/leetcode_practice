pub fn max_profit(prices: Vec<i32>) -> i32 {
    // Initial Solution
    // Time: O(n) | Space: O(1)
    if prices.len() == 1 { return 0 }
    let mut m = prices[0];
    let mut dif = 0;
    for i in 1..prices.len() {
        if (prices[i] - m) > dif {
            dif = prices[i] - m
        } if prices[i] < m {
            m = prices[i]
        }
    }
    dif
}