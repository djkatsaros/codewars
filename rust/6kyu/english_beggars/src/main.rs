/*
 *Born a misinterpretation of this kata, your task here is pretty simple: given an array of values and an amount of beggars, you are supposed to return an array with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last.

For example: [1,2,3,4,5] for 2 beggars will return a result of [9,6], as the first one takes [1,3,5], the second collects [2,4].

The same array with 3 beggars would have in turn have produced a better out come for the second beggar: [5,7,3], as they will respectively take [1,4], [2,5] and [3].

Also note that not all beggars have to take the same amount of "offers", meaning that the length of the array is not necessarily a multiple of n; length can be even shorter, in which case the last beggars will of course take nothing (0).

Note: in case you don't get why this kata is about English beggars, then you are not familiar on how religiously queues are taken in the kingdom ;)

Note 2: do not modify the input array.
 */

fn main() {
    println!("English beggars kata");
}

fn beggars(values: &[u32], n: usize) -> Vec<u32> {
    let mut out = vec![0; n];

    for i in 0..n {

        for e in (i..values.len()).step_by(n) {

            out[i] += values[e]
        }
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic() {
        assert_eq!(beggars(&[1, 2, 3, 4, 5], 1), [15]);
        assert_eq!(beggars(&[1, 2, 3, 4, 5], 2), [9, 6]);
        assert_eq!(beggars(&[1, 2, 3, 4, 5], 3), [5, 7, 3]);
        assert_eq!(beggars(&[1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5, 0]);
    }

    #[test]
    fn test_zero_beggars() { 
        assert_eq!(beggars(&[1, 2, 3, 4, 5], 0), []);

    }
}




