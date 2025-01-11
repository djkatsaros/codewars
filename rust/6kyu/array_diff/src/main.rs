/*
 * Kata description:
 Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.
*/

fn array_diff<T: PartialEq>(a: Vec<T>, b: Vec<T>) -> Vec<T> {
    // Function works by checking if each element el in a is not contained in b. If el is not in b, 
    // add el to the ans in the order they appeared in a.
    // Sets: A - B = (!B) \cap A
    let mut ans = vec![];
    for i in a {
        if !b.contains(&i) { // if b does not contain (address of) i (we dont want the els of b in the answer)
            ans.push(i);
        }
    }
    ans
}

fn main() {
    println!("pass!");
}

// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn returns_expected() {
        assert_eq!(array_diff(vec![1,2], vec![1]), vec![2]);
        assert_eq!(array_diff(vec![1,2,2], vec![1]), vec![2,2]);
        assert_eq!(array_diff(vec![1,2,2], vec![2]), vec![1]);
        assert_eq!(array_diff(vec![1,2,2], vec![]), vec![1,2,2]);
        assert_eq!(array_diff(vec![], vec![1,2]), vec![]);
        assert_eq!(array_diff(vec![1,2,3], vec![1,2]), vec![3]);
    }
}
