### Print the factorial of the integer being supplied as an argument

############################################################
## Internal functions
############################################################

def usage():
    "Print script usage."
    print """
Usage: %s <integer>
    Print the factorial of the <integer>.
""" % argv[0],

def factorial(integer):
    "Return the factorial of the integer."
    if 0 > integer:
        exit('Error: value must be greater or equal to 0.')
    return(factorial_impl(integer, 1))

def factorial_impl(i, acc):
    """Return the factorial of the integer.
    Recursive implementation, use factorial/1."""
    if 0 == i:
        return acc
    return factorial_impl(i - 1, i * acc)


############################################################
## Tests
############################################################

all_tests_pass = True

def assert_equal(expected, form):
    """Assert equality of the form evaluation and expected value.
    In case of failure trigger all_tests_pass global variable to False."""
    value = eval(form)
    if expected != value:
        global all_tests_pass
        all_tests_pass = False
        print """
Fail: %s
expected: %r
value: %r
""" % (form, expected, value)


def tests():
    "Run all internal tests."
    assert_equal(479001600, "factorial(12)")


def check():
    """Check module by running all internal tests.
    Exit script if something fail."""
    global all_tests_pass
    all_tests_pass = True
    tests()
    if False == all_tests_pass:
        exit("Self check failed, can't continue!")


############################################################
## Script 
############################################################

# Running tests
check()

from sys import argv

if len(argv) != 2:
    usage()
    exit(1)

number = int(argv[1])
result = factorial(number)
print result

exit(0)
