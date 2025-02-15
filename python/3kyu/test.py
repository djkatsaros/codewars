"""
https://www.reddit.com/r/learnpython/comments/s1pefg/running_codewars_tests_locally/

Workaround script to allow easier implementation of codewars tests.
See reddit thread for source (mostly, added the message parameter)
"""
def assert_equals(a, b, mess: str ="pass"):
    """
    a: input for the function being tested typically. Non-typed
    b: output for function. No type specfied.
    mess: str type, message if test fails. Default is pass. 

    function calles assert with mess in case of error, and if assertion passes prints the test case equality for a gut check. 
    """
    assert a == b, mess 
    print("Passed test: {} == {}".format(a,b)) 

def assert_approx_equals(a, b, tol,  mess: str = "pass"):
    if abs( a - b ) / b <= tol:
        print("Passed test: {} == {} within tolerance of {}".format(a,b, tol))
    else:
        print(f"Failed. {a} differs from {b} by more than the allowed tolerance of {tol}")

def expect(b: bool, mess: str= "pass"):
    if b:
        print("passed test!")
    else:
        print(mess)
