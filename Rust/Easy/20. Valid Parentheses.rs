// Initial Solution
// Time: 0(n) | Space: O(n)
use std::collections::HashMap;

pub fn is_valid(s: String) -> bool {
    let mut stack = vec!();
    let end_prths = HashMap::from([
        (')', '('),
        ('}', '{'),
        (']', '[')
    ]);

    for p in s.chars() {
        if !end_prths.contains_key(&p) {
            stack.push(p);
        } else if !stack.is_empty() && (&stack[stack.len() - 1] == end_prths.get(&p).unwrap()) {
            stack.pop();
        } else {
            return false;
        }
    }

    stack.is_empty()
}