/*KATA DESCRIPTION
 *The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age,  oldest age].

The order of the numbers passed in could be any order. The array will always include at least 2 items. If there are two or more oldest age, then return both of them in array format.

For example (Input --> Output):

[1, 2, 10, 8] --> [8, 10]
[1, 5, 87, 45, 8, 8] --> [45, 87]
[1, 3, 10, 0]) --> [3, 10]
 */

fn two_oldest_ages(ages: &[u8]) -> [u8; 2] {
    let mut a = [0; 2];
    let max = *ages.iter().max().unwrap();
    let mut max2 = 0;
    let mut ct = 0;
    for el in ages.iter() {
        if *el > max2 && *el < max {
             max2 = *el;
        }
        if *el == max {
            ct += 1
        }
    }
    if ct == 2 {
        a[0] = max;
    }
    else {
        a[0] = max2;
    }
    a[1] = max;

    return a
}

fn main() {
    println!("Two Oldest Kata");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_two_oldest_ages() {
        assert_eq!(two_oldest_ages(&[1, 5, 87, 45, 8, 8]), [45, 87]);
        assert_eq!(two_oldest_ages(&[6, 5, 83, 5, 3, 18]), [18, 83]);
        assert_eq!(two_oldest_ages(&[10, 1]), [1, 10]);
        assert_eq!(two_oldest_ages(&[1, 3, 10, 0]), [3, 10]);
    }
}
