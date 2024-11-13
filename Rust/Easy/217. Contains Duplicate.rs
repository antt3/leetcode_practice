impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut i = 0;
        let mut seen = std::collections::HashSet::new();
        loop {
            if i == nums.len() {
                return false;
            }
            if seen.contains(&nums[i]) {
                return true;
            }
            seen.insert(nums[i]);
            i += 1;
        }
    }
}