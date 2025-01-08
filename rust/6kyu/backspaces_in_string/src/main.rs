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
    for c in s.chars() {
        if c == '#' {
            if out.len() > 0 {
                out.pop();
            }
        } else {
            out.push(c);
        }
    }
    let out_str: String = out.iter().collect();
    out_str
}

/*
 * fn clean_string(s: &str) -> String {
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
