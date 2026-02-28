def factorial (x):
    '''this is a recrusive function to find thr factorial of an integer '''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial (x-1)
print(factorial .__doc__)
print("the factorial of 5:",factorial (6))