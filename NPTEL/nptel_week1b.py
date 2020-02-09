# What is h(36)-h(34), given the definition of h below?

def h(n):
    s = 0
    for i in range(2,n):
        if n%i == 0:
            print(i)
            s = s+i
    return(s)

a=h(36)
b=h(34)
print(a-b)
