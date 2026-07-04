/*
Task

You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).

Input:

If, you can read?

Output:

India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

Note:

    There is a preloaded dictionary that you can use, named NATO. It uses uppercase keys, e.g. NATO['A'] is "Alfa". See comments in the initial code to see how to access it in your language.
    The set of used punctuation is ,.!?.
    Punctuation should be kept in your return string, but spaces should not.
    Xray should not have a dash within.
    Every word and punctuation mark should be seperated by a space ' '.
    There should be no trailing whitespace

The NATO phonetic alphabet (A–Z) is preloaded:

use preloaded::NATO;

NATO[&'R']; // Romeo
NATO[&'U']; // Uniform
NATO[&'S']; // Sierra
NATO[&'T']; // Tango

Click to see the preloaded code

use std::collections::HashMap;
use once_cell::sync::Lazy;

#[rustfmt::skip]
pub static NATO: Lazy<HashMap<char, &'static str>> = Lazy::new(|| {
    [
        ('A', "Alfa"), ('B', "Bravo"), ('C', "Charlie"), ('D', "Delta"),
        ('E', "Echo"), ('F', "Foxtrot"), ('G', "Golf"), ('H', "Hotel"),
        ('I', "India"), ('J', "Juliett"), ('K', "Kilo"), ('L', "Lima"),
        ('M', "Mike"), ('N', "November"), ('O', "Oscar"), ('P', "Papa"),
        ('Q', "Quebec"), ('R', "Romeo"), ('S', "Sierra"), ('T', "Tango"),
        ('U', "Uniform"), ('V', "Victor"), ('W', "Whiskey"), ('X', "Xray"),
        ('Y', "Yankee"), ('Z', "Zulu"),
    ]
    .iter()
    .copied()
    .collect()       
});
*/
mod preloaded;
use preloaded::NATO;

fn to_nato(words: &str) -> String {
    // use NATO HashMap;
    // NATO[&'A'] - "Alpha" etc
    let modified_str: String = words.chars()
        .filter(|c| !c.is_whitespace())
        .collect::<String>()
        .chars()
        .map(|c| c.to_uppercase()
        .to_string())
        .collect();

    modified_str
        .chars()
        .map(|c| match c.is_alphanumeric() {
            true => String::from(NATO[&c]),
            false => c.to_string()
            }).collect::<Vec<String>>()
        .join(" ")
        
}

fn main() {
    println!("Hello, world!");
}

#[cfg(test)]
mod tests {
    use super::to_nato;

    #[test]
    fn examples() {
        assert_eq!(
            to_nato("If you can read"),
            "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta"
        );
        
        assert_eq!(
            to_nato("Did not see that coming",),
            "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf"
        );
        
        assert_eq!(
            to_nato("go for it!"),
            "Golf Oscar Foxtrot Oscar Romeo India Tango !"
        );
    }
}
