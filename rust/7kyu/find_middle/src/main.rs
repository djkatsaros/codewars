/*
 * KATA DESCRIPTION
 *As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers (Haskell: a tuple).

For example:

gimme([2, 3, 1]) => 0

2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.

Another example (just to make sure it is clear):

gimme([5, 10, 14]) => 1

10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.

 */

fn gimme(xs: [i32;3]) -> usize {
    match xs {
        _ if (xs[0] < xs[1]) == (xs[1] < xs[2]) => 1,
        _ if (xs[1] < xs[2]) == (xs[2] < xs[0]) => 2,
        _ => 0
    }
}

fn main() {
    println!("find the middle!");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_gimme() {
        assert_eq!(gimme([2, 3, 1]), 0);
        assert_eq!(gimme([-2, -3, -1]), 0);
        assert_eq!(gimme([5, 10, 14]), 1);
    }
}
