# A positive integer m can be expresseed as the sum of three squares if it is of the form p + q + r where p, q, r ≥ 0,
# and p, q, r are all perfect squares.
# For instance, 2 can be written as 0+1+1 but 7 cannot be expressed as the sum of three squares.
# The first numbers that cannot be expressed as the sum of three squares are 7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, … 
# (see Legendre's three-square theorem).

# Write a Python function threesquares(m) that takes an integer m as input and returns True 
# if m can be expressed as the sum of three squares and False otherwise.
# (If m is not positive, your function should return False.)

from math import *

def threesquares(n):

    for a in range(0,100) :
        for b in range(0,200) :
                c= pow(4,a) * (8 * b) + 7
                if (c==n) :
                    return False
                else :
                    b = b + 1
        a = a + 1

    return True

#  Write a function repfree(s) that takes as input a string s and checks whether any character appears more than once.
#  The function should return True if there are no repetitions and False otherwise.  

def repfree(s):

    n = len(s)

    for i in range(0,n) :
        for j in range(i+1,n) :
            if s[i]==s[j] :
                return False

        return True

# A list of numbers is said to be a hill if it consists of an ascending sequence followed by a descending sequence,
#  where each of the sequences is of length at least two.
#  Similarly, a list of numbers is said to be a valley hill if it consists of an descending sequence followed by 
# an ascending sequence. You can assume that consecutive numbers in the input sequence are always
#  different from each other.
# Write a Python function hillvalley(l) that takes a list l of integers and returns True if it is a hill or a valley, 
# and False otherwise.

def hillvalley(list) :
    
    n = len(list)
    count = 0
    flag = []
    
    for i in range(1,n) :
        if (list[i-1] < list[i]) :
            flag.append(0)
        else :
            flag.append(1)

    
    for i,j in zip(range(0,len(flag)-1), range(1,len(flag))):
    	if flag[i] != flag[j] :
            count = count + 1


    
    if (count == 1) :
        return True

    return False
    
