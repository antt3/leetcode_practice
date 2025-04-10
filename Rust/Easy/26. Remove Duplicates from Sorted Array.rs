pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
    // Initial Solution
    if nums.len() == 1 {return 1}
    let mut k = 1;
    let mut i = 1;
    for j in 1..nums.len() {
        if j == nums.len() {return k}
        if nums[j] > nums[i - 1] {
            nums[i] = nums[j];
            i += 1;
            k += 1;
        }
    }
    k
}