pub fn is_palindrome(s: String) -> bool {
    // Initial Solution
    // Time: O(n) | Space: O(n)
    let a = std::collections::HashMap::from([
        ('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'), ('E', 'e'), ('F', 'f'), ('G', 'g'), ('H', 'h'), ('I', 'i'), ('J', 'j'), ('K', 'k'), ('L', 'l'), ('M', 'm'), ('N', 'n'), ('O', 'o'), ('P', 'p'), ('Q', 'q'), ('R', 'r'), ('S', 's'), ('T', 't'), ('U', 'u'), ('V', 'v'), ('W', 'w'), ('X', 'x'), ('Y', 'y'), ('Z', 'z')
    ]);
    if s.len() < 2 { return true }
    let s : Vec<char> = s.chars().collect();
    let mut l = 0;
    let mut r = s.len() - 1;
    while l < r {
        let l_char = if a.contains_key(&s[l]) { a[&s[l]] } else { s[l] };
        let r_char = if a.contains_key(&s[r]) { a[&s[r]] } else { s[r] };
        if l_char.is_alphanumeric() && r_char.is_alphanumeric() {
            if l_char == r_char {
                l = l + 1;
                r = r - 1;
                continue
            } else {
                return false
            }
        }
        if !l_char.is_alphanumeric() { l = l + 1 }
        if !r_char.is_alphanumeric() { r = r - 1 }
    }
    true
}