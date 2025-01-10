/* KATA DESCRIPTION
 * In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

    Years divisible by 4 are leap years,
    but years divisible by 100 are not leap years,
    but years divisible by 400 are leap years.

Tested years are in range 1600 ≤ year ≤ 4000.
 *
 */

fn is_leap_year(year: i32) -> bool {
    let mut leap: bool = false;
    
    if year % 100 == 0 {
        if year % 400 == 0 {
            leap = true;
            }
    }
    else {
        if year % 4 == 0 {
            leap = true;
        }
    }
    
    leap
}

fn main() {
    println!("Leap years kata");
}

#[cfg(test)]
mod sample_tests {
    use super::is_leap_year;

    fn do_test(year: i32, expected: bool) {
        let actual = is_leap_year(year);
        assert_eq!(actual, expected, "\nYour result (left) does not match the expected output (right) for the year {year:?}");
    }

    #[test]
    fn year_2020_is_a_leap_year() {
        do_test(2020, true);
    }

    #[test]
    fn year_2000_is_a_leap_year() {
        do_test(2000, true);
    }

    #[test]
    fn year_2015_is_not_a_leap_year() {
        do_test(2015, false);
    }

    #[test]
    fn year_2100_is_not_a_leap_year() {
        do_test(2100, false);
    }
}
