# Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, 
# keeping only the first occurrence of each number.

def remdup(l) :
    res = [] 
    for i in l: 
        if i not in res: 
            res.append(i)
        
    return res

# Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even],
# where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l.


def sumsquare(l) :
    sum_sq=[0,0]
    for i in l:
        if i%2==0 :
            sum_sq[1] += i**2
        else :
            sum_sq[0] += i**2

    return sum_sq

# A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row
# of the matrix.

def transpose(m) :
    m= [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return m

    




