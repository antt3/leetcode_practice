pub fn climb_stairs(n: i32) -> i32 {
    // Initial Solution
    if (n <= 2) {
        n
    } else {
        Self::climb_stairs(n - 2) + Self::climb_stairs(n - 1)
    }
}