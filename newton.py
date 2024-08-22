def function(x): 
    """define f(x)=x^2 +10"""
    return float (x**2)+ 10
    
epsilon=0.000000005 
def derivative(x): 
    """Take the derivative of function f(x) at x"""
    return float(function(x + epsilon) - function (x))/epsilon 

def newton_method(x, func): 
    """Do Newton's method for the function passed

    Keyword arguments:
    x -- x value to guess as a starting point for the global minimum
    func -- the function
    """
    x_t_1 = x 
    x_t =0
    while True: 
        d1 = derivative(x) 
        print(d1) 
        d2 =((derivative(x) + epsilon)-derivative(x))/ epsilon
        print(d2) 
        x_t = x_t_1 - (d1/d2)
        print(x_t) 
        if abs(x_t-x_t_1) <0.0001:
            break 
        x_t_1 = x_t 
        return x_t

newton_method(5, function)