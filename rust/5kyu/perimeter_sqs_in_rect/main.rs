/*
 * The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:
*/



fn perimeter(n: u64) -> u64 {
    /* clever way to do recursion
     (0..n) is an iterator.
     fold ( initital value, closure|a: "accumulator", element|)
     here the closure is entrywise operators on a tuple of length = the number of entries
     in the recursion we need to keep track of.
     For ex. for Fib, need 3 entries. a_{n-2}, a{n-1} + a_{n-2}, and a_n + a_{n-1}.
    */
    let m = (0..n).fold((1u64, 1u64, 1u64), |a, _| (a.1, a.0 + a.1, a.1 + a.2)); //.2 * 4
    println!("({},{},{})", m.0,m.1,m.2);
    m.2 * 4
}

/*alternate solution using alternate method of computing fib sequence
 * fn perimeter(n: u64) -> u64 {
  // your code
    let mut _fib = 1;
    let mut tot = 1;
    let mut a = 0;
    let mut b = 0;

    for i in 1..n+1 {
        a = b;
        b = _fib;
        _fib = a + b;
        tot += _fib;

    }
    tot = 4 * tot;
    tot
}
 *
 * */

fn dotest(n: u64, exp: u64) -> () {
    assert_eq!(perimeter(n), exp, "test failed perimeter of {} +1 squares is {}", n, exp)
}   

fn main() {
    println!("testing");
    dotest(5, 80);
    dotest(7, 216);
    dotest(20, 114624);
    dotest(30, 14098308);

    dotest(40, 1733977744);
    dotest(50, 213265164688);
    dotest(60, 26229881279364);
    dotest(70, 3226062132197568);

    dotest(16, 16720);
    dotest(67, 761569962836536);
    dotest(64, 179782280851408);
    dotest(46, 31114968192);
    dotest(3, 28);
    dotest(22, 300096);
    dotest(39, 1071657180);
    dotest(55, 2365146919512);
    dotest(22, 300096);
    dotest(19, 70840);
    dotest(15, 10332);
    dotest(39, 1071657180);
    dotest(32, 36909856);
    dotest(16, 16720);
    dotest(36, 252983940);
    dotest(7, 216);
    dotest(3, 28);
    dotest(44, 11884860288);
    dotest(15, 10332);
    dotest(9, 572);
    dotest(44, 11884860288);
    dotest(35, 156352672);
    dotest(17, 27056);
    dotest(17, 27056);
    dotest(3, 28);
    dotest(22, 300096);
    dotest(42, 4539612676);
    dotest(10, 928);
    dotest(49, 131805120392);
    dotest(26, 2056912);
    dotest(5, 80);
    dotest(65, 290893840992560);
    dotest(48, 81460044292);
    dotest(53, 903405734864);
    dotest(42, 4539612676);
    dotest(4, 48);
    dotest(37, 409336616);
    dotest(31, 22811544);
    dotest(67, 761569962836536);
    dotest(55, 2365146919512);
    dotest(36, 252983940);
    dotest(56, 3826888104160);
    dotest(43, 7345247608);

    dotest(10, 928);
    dotest(32, 36909856);
    dotest(12, 2436);
    dotest(63, 111111560141148);
    dotest(45, 19230107900);
    dotest(62, 68670720710256);
    dotest(53, 903405734864);
    dotest(61, 42440839430888);
    dotest(21, 185468);
    dotest(60, 26229881279364);
    dotest(5, 80);
    dotest(24, 785668);
    dotest(30, 14098308);
    dotest(13, 3944);
    dotest(34, 96631264);
    dotest(35, 156352672);
    dotest(45, 19230107900);
    dotest(7, 216);
    dotest(47, 50345076096);
    dotest(44, 11884860288);
    dotest(32, 36909856);
    dotest(29, 8713232);
    dotest(28, 5385072);
    dotest(63, 111111560141148);
    dotest(22, 300096);
    dotest(52, 558335449776);
    dotest(37, 409336616);
    dotest(21, 185468);
    dotest(25, 1271240);
    dotest(15, 10332);
    dotest(11, 1504);
    dotest(20, 114624);
    dotest(60, 26229881279364);
    dotest(48, 81460044292);
    dotest(3, 28);
    dotest(66, 470676121843972);
    dotest(7, 216);
    dotest(13, 3944);
    dotest(57, 6192035023676);
    dotest(49, 131805120392);
    dotest(3, 28);
    dotest(14, 6384);
    dotest(41, 2805634928);
    dotest(53, 903405734864);
    dotest(67, 761569962836536);
    dotest(42, 4539612676);
    println!("Passed all tests"); 
}


