'''
lambda is needed only when you want a custom operation that doesn’t already exist as a function.
eg: lambda x: x[1] → get second element of a tuple
'''
# lambda in Python is just a shortcut to define a small, anonymous function — a function without a name.
'''
# Syntax of lambda
lambda parameters: expression
No need to use def or give it a name
'''
def f(x): return x**2

""" Equivalent to :-
def f(x):
    return x**2
"""

print(f(5))  # 25
