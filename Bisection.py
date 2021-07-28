from sympy import *


def function(y):
    x = symbols('x')
    return expr.subs(x, y)


def bisection(a, b, tolerance):
    if function(a) * function(b) >= 0:
        print("You have not assumed right a and b\n")
        return

    i = 1
    print(
        "Iteration\t\t\t" + " Left\t\t\t" + " Right\t\t\t" + " Middle\t\t\t" + " f(Left)\t\t\t" + " f(Right)\t\t\t" + " f(Middle)\t\t\t" + " ea")

    while (b - a) >= tolerance:

        xnew = (a + b) / 2
        funca = function(a)
        funcb = function(b)
        funcc = function(xnew)

        if i == 1 or xnew == 0:
            print("%d\t\t\t\t\t" % i, "{:.2f}".format(a), "\t\t\t", "{:.2f}".format(b), "\t\t\t",
                  "{:.2f}".format(xnew), "\t\t\t", "{:.2f}".format(funca), "\t\t\t",
                  "{:.2f}".format(funcb), "\t\t\t\t", "{:.2f}".format(float(funcc)))
        else:
            print("%d\t\t\t\t\t" % i, "{:.2f}".format(a), "\t\t\t", "{:.2f}".format(b), "\t\t\t",
                  "{:.2f}".format(xnew), "\t\t\t", "{:.2f}".format(funca), "\t\t\t\t",
                  "{:.2f}".format(float(funcb)), "\t\t\t\t", "{:.2f}".format(funcc), "\t\t\t\t", "{:.2f}".format(xnew - prev))

        i = i + 1
        if funcc == 0.0:
            break

        if funcc * funca < 0:
            b = xnew
        else:
            a = xnew

        prev = xnew

    print("The root is at : ", "%.8f" % xnew)


From = input('Enter the start of the range:- ')

To = input('Enter the end of the range:- ')

Tolerance = input('Enter the required tolerance:- ')

Function = input('Enter a function:- ')
expr = sympify(Function)

print(f'Bisection Method  [{From},{To}]  with Tolerance =  {Tolerance}')
bisection(float(From), float(To), float(Tolerance))
