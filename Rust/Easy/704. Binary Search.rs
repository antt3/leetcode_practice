pub fn search(nums: Vec<i32>, target: i32) -> i32 {
    // Initial Solution
    // Time: O(log(n)) | Space O(1)
    let mut l = 0;
    let mut r = nums.len();

    while l < r {
        let m = l + ((r - l) / 2);
        if target > nums[m] {
            l = m + 1;
        } else if target < nums[m] {
            r = if m == 0 {
                m
            } else {
                m - 1
            }
        } else {
            return m as i32;
        }
    }

    if l < nums.len() && nums[l] == target {
        l as i32
    } else {
        -1
    }
}