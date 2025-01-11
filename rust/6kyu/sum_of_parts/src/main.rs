/*Let us consider this example (array written in general format):

ls = [0, 1, 3, 6, 10]

Its following parts:

ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []

The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of the sums of its parts as defined above.
Other Examples:

ls = [1, 2, 3, 4, 5, 6] 
parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
*/

fn parts_sums(ls: &[u64]) -> Vec<u64> {
    let mut vec = vec![ls.iter().sum()]; // initialize out vector as a heap (!) with the sum of the inputed list (first entry of the output will be the total sum)
    for item in ls {
        vec.push(vec[vec.len()-1] - item); // add to vec the most recently added entry of the vector minus next entry of the inputed list. 
    }
    vec
}
/*
Example:
ls = [1,2,3,4,5,6]
loop number  | vec
------------------
0            | [21]
1            | [21, ( 21 - 1 = 20 ) ]
2            | [21, 20, ( 20 - 2 = 18 ) ]
3            | [21, 20, 18, ( 18 - 3 = 15 ) ]
4            | [21, 20, 18, 15, ( 15 - 4 = 11 ) ]
.            |    .
.            |    .
.            |    .
*/

fn main() {
    println!("Sum of parts kata in rust!");
    println!("Type 'cargo test' to run tests. Add your own tests too");
}

#[cfg(test)]
mod tests {
    use super::*;
    
    fn dotest(ls: Vec<u64>, expect: Vec<u64>) {
        let actual = parts_sums(&ls);
        assert_eq!(actual, expect);
    }
    
    #[test]
    fn example() {
        dotest(vec![], vec![0]);
        dotest(vec![0, 1, 3, 6, 10], vec![20, 20, 19, 16, 10, 0]); 
        dotest(vec![1, 2, 3, 4, 5, 6], vec![21, 20, 18, 15, 11, 6, 0]);     
        dotest(vec![744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358], 
            vec![10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]); 
    }
}
