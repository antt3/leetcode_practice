// 217. Contains Duplicate
// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Example 1:
// Input: nums = [1,2,3,1]
// Output: true

// Example 2:
// Input: nums = [1,2,3,4]
// Output: false

// Example 3:
// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true

// Constraints:
//     1 <= nums.length <= 105
//     -109 <= nums[i] <= 109

bool containsDuplicate(int* nums, int numsSize) {
    // Create 2 pointers
    int p1 = 0;
    int p2 = 1;

    // Use a while loop to increment the 2nd pointer
    // If the both pointers reach the last 2 indexes of the list exit the while loop
    while (p2 < numsSize) {

        // If the value at each pointer is ever the same RETURN true
        if (nums[p1] == nums[p2]) {
            return true;
        }

        // If the 2nd pointer reaches the end of the array, increment 1st pointer, reset 2nd pointer
        if (p2 < numsSize - 1) {
            p2++;
        } else {
            p1++;
            p2 = p1 + 1;
        }
    }
    
    // If the while loop completes RETURN false
    return false;
}