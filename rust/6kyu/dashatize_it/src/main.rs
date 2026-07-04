/*Given an integer, return a string with dash '-' marks before and after each odd digit, but do not begin or end the string with a dash mark.

Ex:

274 -> '2-7-4'
6815 -> '68-1-5'
*/

fn dashatize(n: i64) -> String {
    let n_: String = n.abs().to_string();
    let len_: usize = n_.len() - 1;
    let mut out: String = String::from("");
    out = n_.chars()
            .enumerate()
            .map(|(idx, c)|
                match c.to_digit(10).unwrap() % 2 == 0 {
                    true => String::from(c),
                    false => if idx == 0
                    {
                        format!("{}-", c)
                    } else if idx == len_
                    {
                        format!("-{}", c)
                    } else
                    {
                        format!("-{}-", c)
                    }
                }).collect::<String>();
    if out.chars().nth(out.len() - 1).unwrap() == '-'
    {
        out.pop();
    }
    out.replace("--", "-")
}

fn main() {
    println!("Hello, world!");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn basic() {
        assert_eq!(dashatize(274), "2-7-4");
        assert_eq!(dashatize(5311), "5-3-1-1");
        assert_eq!(dashatize(86320), "86-3-20");
        assert_eq!(dashatize(974302), "9-7-4-3-02");
    }
    
    #[test]
    fn weird() {
        assert_eq!(dashatize(0), "0");
        assert_eq!(dashatize(-1), "1");
        assert_eq!(dashatize(-28369), "28-3-6-9");                
    }
}
