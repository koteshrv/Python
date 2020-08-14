# even or odd function
def even(n):
    if n % 2 == 0:
        return True
    return False

# max of three
def unique(lst):
    l = []
    for i in lst:
        if lst.count(i) == 1:
            l.append(i)
    print(l)