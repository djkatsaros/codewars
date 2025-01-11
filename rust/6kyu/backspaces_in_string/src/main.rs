/*
 * Kata description:
 *
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.
Examples

"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
*/
fn main() {
    println!("pass!");
}

fn clean_string(s: &str) -> String {
    let mut out: Vec<char> = Vec::new();
    for c in s.chars() { // iterate over the char iterater. 
        if c == '#' {
            if out.len() > 0 {
                out.pop(); // delete last entry if current char is == '#'
            }
        } else {
            out.push(c); // push the char c otehrwise
        }
    }
    let out_str: String = out.iter().collect(); // make an iterator, and collect into a string. (makes a string from a list)
    out_str
}

/*
 * // ALternate, slicker soluition using a fold. Essentially does the above in 1 line and without having to use collect after 
fn clean_string(s: &str) -> String {
     // fold the char iterator of s into acc(umulator) based on the conditional that we pop (delete last entry) of acc if the current char c is == '#', and add c otherwise
    s.chars().fold(String::new(), |mut acc, c| if c == '#' {acc.pop(); acc} else {acc.push(c); acc})
}
 */
// tests

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sample_tests() {
        assert_eq!(clean_string("abc#d##c"), "ac");
        assert_eq!(clean_string("abc####d##c#"), "");
        assert_eq!(clean_string("#######"), "");
        assert_eq!(clean_string(""), "");
    }
}
