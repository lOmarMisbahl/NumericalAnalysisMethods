import math
from sympy import *
MAX_ITER = 1000000


# An example function whose solution
# is determined using Bisection Method.
# The function is x^3 - x^2 + 2
from sympy import *

f = input('Enter a function:- ')
expr = sympify(f)


def function(y):
    x = symbols('x')
    return expr.subs(x, y)


# Prints root of func(x) in interval [a, b]
def regulaFalsi(a, b, tolerance):
    if function(a) * function(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c = a  # Initialize result
    print(
        "Iteration\t" + " Left\t\t\t" + " Right\t\t\t" + " Middle\t\t\t" + " f(Left)\t\t\t" + " f(Right)\t\t\t" + "  f(Middle)\t\t\t" + " ea")

    for i in range(MAX_ITER):

        funca = function(a)
        funcb = function(b)
        prev = c;
        # Find the point that touches x axis
        c = (a * funcb - b * funca) / (funcb - funca)

        new = c
        funcc = function(c)

        if i == 0 or new == 0 :
            print("%d\t\t\t" % i, round(a,2), "\t", round(b,2), "\t",
                  round(c,2), "\t",round(funca,2), "\t",
                  round(funcb,2),
                  "\t", round(funcc,2), "\t")
        else:
            print("%d\t\t\t" % i, round(a,2), "\t", round(b,2), "\t",
                  round(c,2), "\t", round(funca,2), "\t",
                  round(funcb,2),
                  "\t", round(funcc,2), "\t", round(((new - prev) / new) * 100,2))

        # Check if the above found point is root
        if funcc == 0:
            break

        if abs(new - prev) < tolerance:
            break;
        # Decide the side to repeat the steps
        elif funcc * funca < 0:
            b = c
        else:
            a = c

        prev = c;

    print("The value of root is : ", '%.4f' % c)


def sci_notation(number, sig_fig=2):
    ret_string = "{0:.{1:d}e}".format(number, sig_fig)
    a, b = ret_string.split("e")
    b = int(b)  # removed leading "+" and strips leading zeros too.
    return a + " * 10^" + str(b)


# Driver code
a = -2
b = 0

print("Regula Falsi Method  [-1,-3]")

regulaFalsi(a, b, 0.0001)
