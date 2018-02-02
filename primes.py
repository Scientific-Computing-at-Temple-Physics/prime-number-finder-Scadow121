# This is a comment.  Python will ignore these lines (starting with #) when running

import math as ma
import time
# To use a math function, write "ma." in front of it.  Example:  ma.sin(3.146)

# These functions will ask you for your number ranges, and assign them to 'x1' and 'x2'
x1 = raw_input('smallest number to check: ')
x2 = raw_input('largest number to check: ')

# This line will print your two numbers out
print x1, x2

""" Text enclosed in triple quotes is also a comment.
This code should find and output all prime numbers between (and including) the numbers entered initially.
If no prime numbers are found in that range, it should print a statement to the user.
Now we end the comment with triple quotes."""

# The rest is up to you!

x1=int(x1)
x2=int(x2)
if x1 < x2:
    print "The prime numbers between" ,x1, "and" ,x2, "are:"
    x = x1
    d = 2
    while x != (x2+1):
        if x != d:
            q = x%d
            if q != 0:
                if d >= x:
                    if x > 0:
                        print x
                        x = x+1
                        d = 2
                    else:
                        x = x+1
                        d = 2
                else:
                    d = d+1
            else:
                x = x+1
                d = 2
        else:d = d+1
else:
    print "Invalid Input Detected!"
    time.sleep(0.5)
    print "Initiating Self-Destruct Sequence (This may take a while)..."
    time.sleep(10)
