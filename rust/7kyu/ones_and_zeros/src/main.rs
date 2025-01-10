/*KATA DESCRIPTION
 *Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11

However, the arrays can have varying lengths, not just limited to 4.

 */

fn binary_slice_to_number(slice: &[u32]) -> u32 {
    // your code here
    let mut pow_ = 0;
    let mut sum_ = 0;
    let base = 2u32;
    let len_ = slice.len() as u32;
    for &i in slice{
        if i != 0 {
            sum_ += base.pow(len_ - pow_ - 1);
            }
        pow_ += 1;
        }
    sum_
}

fn main() {
    println!("ONes and zeros Kata");
}

#[cfg(test)]
mod tests {
    use super::binary_slice_to_number;

    #[test]
    fn example_tests() {
      assert_eq!(binary_slice_to_number(&vec![0,0,0,1]), 1);
      assert_eq!(binary_slice_to_number(&vec![0,0,1,0]), 2);
      assert_eq!(binary_slice_to_number(&vec![1,1,1,1]), 15);
      assert_eq!(binary_slice_to_number(&vec![0,1,1,0]), 6);
    }
}
