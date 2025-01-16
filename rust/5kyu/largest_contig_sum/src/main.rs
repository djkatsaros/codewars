/*
 * Kata Description
 * Given an array of numbers, calculate the largest sum of all possible blocks of consecutive elements within the array. The numbers will be a mix of positive and negative values. If all numbers of the sequence are nonnegative, the answer will be the sum of the entire array. If all numbers in the array are negative, your algorithm should return zero. Similarly, an empty array should result in a zero return from your algorithm.

largestSum([-1,-2,-3]) == 0
largestSum([]) == 0
largestSum([1,2,3]) == 6

Easy, right? This becomes a lot more interesting with a mix of positive and negative numbers:

largestSum([31,-41,59,26,-53,58,97,-93,-23,84]) == 187

The largest sum comes from elements in positions 3 through 7: 59+26+(-53)+58+97 == 187

Once your algorithm works with these, the test-cases will try your submission with increasingly larger random problem sizes.

 */
use std::cmp;

fn main() {
    println!("Kadane's Algorithm!");
}

fn largest_sum(arr: &[i32]) -> i32 {
    //Kadane's algorithm
    let mut max_out = 0i32;
    let mut max_temp = 0i32;
    for &item in arr {
        max_temp = cmp::max(item, max_temp + item); 
        max_out = cmp::max(max_out, max_temp);
    }
    
    max_out
}
//
#[cfg(test)]
mod tests {
    use super::largest_sum;

    fn dotest(a: &[i32], expected: i32) {
        let actual = largest_sum(a);
        assert!(actual == expected,
            "With arr = {a:?}\nExpected {expected} but got {actual}")
    }
}
