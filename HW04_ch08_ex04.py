#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body

#Correct
def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

#Incorrect.Doesnt iterate over the actual string but only checks a static string with value 'c'
def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

#Incorrect. Only returns the status of the last element in the string
def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        flag = c.islower()
    return flag

#Corret
def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

#Incorrect. The return statement will exit the entire function. If we encounter
# an uppercase letter first, the function will just exit without checking the
# other elements.
def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print("Hello World!")
    print(any_lowercase2("AVIDIXIT"))
    print(any_lowercase3("avidixiT"))
    print(any_lowercase5("Avidixit"))
    

if __name__ == '__main__':
    main()
