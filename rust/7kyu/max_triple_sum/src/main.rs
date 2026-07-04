/*Task

Given an array/list of integers, find the maximum sum of 3 DISTINCT array elements.
Notes :

    array size is at least 3 .
    array elements can be zero or negative
    Repetition of numbers in the array/list could occur , So (duplications are not included when summing).

Input >> Output Examples

    maxTriSum ({3,2,6,8,2,3}) ==> return (17)

    Best triplet = {6,8,3}, its sum is 17

    maxTriSum ({2,1,8,0,6,4,8,6,2,4}) ==> return (18)

    Best triplet = {8, 6, 4} , its sum is 18.

    maxTriSum ({-7,12,-7,29,-5,0,-7,0,0,29}) ==> return (41)

    Best triplet = {12 , 29 , 0} , its sum is 41
*/

// two solutions
use itertools::Itertools;
use std::collections::BTreeSet;

fn max_tri_sum1(xs: &[i32]) -> i32 {
    xs.iter().sorted().rev().dedup().take(3).sum() //nice
}

fn max_tri_sum2(arr: &[i32]) -> i32 {
    let mut A: BTreeSet<i32> = BTreeSet::new(); // use a Set implement via binary tree for
                                                // O(1) searching
    let mut max1: i32 = -100000000;
    let mut max2: i32 = -100000000;
    let mut max3: i32 = -100000000;
    A.insert(max1);
    A.insert(max2);
    A.insert(max3);
    for idx in 0..arr.len()
    {
        if arr[idx] > max1 && !A.contains(&arr[idx])
        {
            max3 = max2;
            max2 = max1;
            max1 = arr[idx];
            A.insert(max1);
            A.insert(max2);
            A.insert(max3);
        } else if arr[idx] > max2 && !A.contains(&arr[idx])
        {
            max3 = max2;
            max2 = arr[idx];
            A.insert(max2);
            A.insert(max3);
        } else if arr[idx] > max3 && !A.contains(&arr[idx])
        {
            max3 = arr[idx];
            A.insert(max3);
        }
    }
    max1 + max2 + max3
}

fn main() {
    println!("Hello, world!");
}

#[cfg(test)]
mod tests1 {
    use super::*;

    #[test]
    fn basic() {
        assert_eq!(max_tri_sum1(&[3,2,6,8,2,3]),17);
        assert_eq!(max_tri_sum1(&[2,9,13,10,5,2,9,5]),32);
        assert_eq!(max_tri_sum1(&[2,1,8,0,6,4,8,6,2,4]),18);
        assert_eq!(max_tri_sum1(&[-3,-27,-4,-2,-27,-2]),-9);
        assert_eq!(max_tri_sum1(&[-14,-12,-7,-42,-809,-14,-12]),-33);
        assert_eq!(max_tri_sum1(&[-13,-50,57,13,67,-13,57,108,67]),232);
        assert_eq!(max_tri_sum1(&[-7,12,-7,29,-5,0,-7,0,0,29]),41);
        assert_eq!(max_tri_sum1(&[-2,0,2]),0);
        assert_eq!(max_tri_sum1(&[-2,-4,0,-9,2]),0);
        assert_eq!(max_tri_sum1(&[-5,-1,-9,0,2]),1);        
    }
}
#[cfg(test)]
mod tests2 {
    use super::*;

    #[test]
    fn basic() {
        assert_eq!(max_tri_sum2(&[3,2,6,8,2,3]),17);
        assert_eq!(max_tri_sum2(&[2,9,13,10,5,2,9,5]),32);
        assert_eq!(max_tri_sum2(&[2,1,8,0,6,4,8,6,2,4]),18);
        assert_eq!(max_tri_sum2(&[-3,-27,-4,-2,-27,-2]),-9);
        assert_eq!(max_tri_sum2(&[-14,-12,-7,-42,-809,-14,-12]),-33);
        assert_eq!(max_tri_sum2(&[-13,-50,57,13,67,-13,57,108,67]),232);
        assert_eq!(max_tri_sum2(&[-7,12,-7,29,-5,0,-7,0,0,29]),41);
        assert_eq!(max_tri_sum2(&[-2,0,2]),0);
        assert_eq!(max_tri_sum2(&[-2,-4,0,-9,2]),0);
        assert_eq!(max_tri_sum2(&[-5,-1,-9,0,2]),1);        
    }
}
