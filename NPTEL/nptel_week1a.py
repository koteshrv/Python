# What is the value of f(4000) for the function below?

def f(x):
    d=0
    while x >= 1:
        (x,d) = (x/5,d+1)
    return(d)

print(f(4000))