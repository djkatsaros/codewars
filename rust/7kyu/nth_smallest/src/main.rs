/*
Description:

Introduction and warm-up (highly recommended): Playing With Lists/Arrays Series
Task

Given an array/list of integers, find the Nth smallest element in the array.
Notes

    Array/list size is at least 3.
    Array/list's numbers could be a mixture of positives , negatives and zeros.
    Repetition in array/list's numbers could occur, so don't remove duplications.

Input >> Output Examples

arr=[3,1,2]            n=2    ==> return 2 
arr=[15,20,7,10,4,3]   n=3    ==> return 7 
arr=[2,169,13,-5,0,-1] n=4    ==> return 2 
arr=[2,1,3,3,1,2],     n=3    ==> return 2 

*/


use itertools::Itertools;

fn nth_smallest(nums: &[i32], pos: usize) -> i32 {
    *nums.iter().sorted().skip(pos - 1).next().unwrap()
}

fn main() {
    println!("Hello, world!");
}

// https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sample_tests() {
        assert_eq!(nth_smallest(&[3, 1, 2], 2), 2);
        assert_eq!(nth_smallest(&[15, 20, 7, 10, 4, 3], 3), 7);
        assert_eq!(nth_smallest(&[-5, -1, -6, -18], 4), -1);
        assert_eq!(nth_smallest(&[-102, -16, -1, -2, -367, -9], 5), -2);
        assert_eq!(nth_smallest(&[2, 169, 13, -5, 0, -1], 4), 2);
    }
}
