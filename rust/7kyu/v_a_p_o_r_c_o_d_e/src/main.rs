/*ASC Week 1 Challenge 4 (Medium #1)

Write a function that converts any sentence into a V A P O R W A V E sentence. a V A P O R W A V E sentence converts all the letters into uppercase, and adds 2 spaces between each letter (or special character) to create this V A P O R W A V E effect.

Note that spaces should be ignored in this case.
Examples

"Lets go to the movies"       -->  "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
"Why isn't my code working?"  -->  "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"
*/

fn vaporcode(s: &str) -> String {
    let vapor: String = s.chars()
    .filter(|c| !c.is_whitespace())
    .collect::<String>()
    .chars()
    .map(|c| c.to_uppercase().to_string())
    .collect::<Vec<String>>()
    .join("  ");
    vapor
}

fn main() {
    println!("H e l l o, V A P O R w o r l d!");
}

// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_examples() {
        assert_eq!(vaporcode("Lets go to the movies"), "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S".to_string());
        assert_eq!(vaporcode("Why isn't my code working?"), "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?".to_string());
    }
}
