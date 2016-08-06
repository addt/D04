# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

def rotate(s,n):
    new_s = ""
    for i in s:
        new_s = new_s + chr(((ord(i) - 97) + n)%26 + 97)
    print(new_s)

rotate("xyz",2)
rotate("xyz",28)
rotate("xyz",54)
rotate("def",-6)
rotate("def",-32)
