import random
import math
# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""


    def randomer():
        a = random.uniform(-1,1)
        return a
    alpha = randomer()
    beta = random.choice([1,2,3,4,5,6])

    def expr_1(x,y):
        w = math.lgamma(alpha) / math.cos(x) * math.sin(y)
        q = ((math.sin(alpha) * math.cos(y)) * math.sin(y-x) * math.gamma(alpha)) * math.tan(y)
        return (((q * (math.acos(y)) * ((math.sqrt(math.pi*math.e))) % math.pi)) *(w**2))

    def expr_2(x,y):
        a = math.gamma(alpha) * math.tan(x) * math.cos(y)
        return ((a**9) * (y**2)) % math.cos(a)

    def expr_3(x, y):
        b = ((math.pi % alpha) * x**3) / math.fabs(alpha)
        c = (math.tan(math.cos(math.cos((b * math.cos(y))* math.pi)))) * math.gamma(alpha % math.e)
        d = ((math.sin((c * math.gamma(alpha)) % math.e)) * math.tan(alpha))
        return math.sin(d * expr_2(x,y)) * expr_1(x,y)

    def expr_4(x,y):
        return expr_3(x,y) * math.cos(expr_1(x,y)) % math.gamma(alpha)

    def expr_5(x,y):
        a = math.cos(math.tan(x)) % (alpha * math.cos(math.pi))
        b = a / math.acos(y)
        c = b * math.lgamma(a)
        d = math.sin(alpha)**5
        return (d / c) * expr_2(x,y)
    def expr_6(x, y):
        return expr_5(x,y) * expr_4(x,y) * (expr_1(x,y)) * math.gamma(alpha)
    def expr_7(x,y):
        return math.sin(((((((expr_1(x,y) ** 2) - alpha) ** 3) - alpha) ** 2) - (alpha)))

    """def expr_4(x, y):
        gama = [math.sin(x), math.sin(y), math.sin(alpha)]
        delta = [math.cos(x), math.cos(y), math.cos(alpha)]
        upsilon = [math.tan(x), math.tan(y), math.tan(alpha)]
        #eta = [math.gamma(x), math.gamma(y), math.gamma(alpha)]
        t = random.choice(gama)
        h = random.choice(delta)
        e = random.choice(upsilon)
        #n = random.choice(eta)
        then = [t, h, e]
        th_en = random.choice(then)
        return th_en*th_en*th_en*th_en"""

    if beta == 1:
        return expr_1
    elif beta == 2:
        return expr_2
    elif beta == 3:
        return expr_3
    elif beta == 4:
        return expr_4
    elif beta == 5:
        return expr_5
    elif beta == 6:
        return expr_6
    elif beta == 7:
        return expr_7



def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
