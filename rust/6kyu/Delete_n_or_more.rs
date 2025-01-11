/*Task

Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
With list [20,37,20,21] and number 1, the result would be [20,37,21]. 
*/

fn delete_nth(lst: &[u8], n: usize) -> Vec<u8> {
    let mut out = vec![];
    for l in lst {
        // convert out to an iter object. Filter (addresses of) n such that n == l, then count the result.
        // if the count is less than n, push (dereferenced) l into out. 
        if out.iter().filter(|&n| n == l).count() < n {
            out.push(*l);
        }
    }
    out
}
