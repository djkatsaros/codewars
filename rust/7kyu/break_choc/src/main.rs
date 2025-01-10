/*KATA DESCRIPTION
 * Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.

For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break, but for size 3 x 1 you must do two breaks.

If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). Input will always be a non-negative integer.
 *
 */

fn break_chocolate(n: u32, m: u32) -> u64 { 
    if n == 0 || m == 0 { 0 } 
    else { 
        (n as u64) * (m as u64) - 1 }
    
}


fn main() {
    println!("break chocolate kata");
}

// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::break_chocolate;

    fn dotest(n: u32, m: u32, expected: u64) {
        let actual = break_chocolate(n, m);
        assert!(actual == expected,
            "With n = {n}, m = {m}\nExpected {expected} but got {actual}")
    }

    #[test]
    fn fixed_tests() {
        dotest(5, 5, 24);
        dotest(7, 4, 27);
        dotest(1, 1, 0);
        dotest(0, 0, 0);
        dotest(6, 1, 5);
    }
}

