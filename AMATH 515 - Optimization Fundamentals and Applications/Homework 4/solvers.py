import numpy as np

#Throughout this code,you may want to modify the structure of these functions to 
#include additional parameters such as stopping tolerance or maximum iterations!

def bisection_linesearch(x,d,f,gradf,c0,c1,t0=1.):
    """

    Parameters
    ----------
    x : Previous iterate
    d : Search direction
    f : Objective function
    gradf : Gradient of objective function
    c0 : Parameter for W1 condition (you may want to set a default)
    c1 : Parameter for W2 condition (you may want to set a default)
    t0 : Initial stepsize, by default 1.

    Returns
    -------
    alpha: accepted line search stepsize
    fval: function value at location of accepted step
    g: gradient at the location of accepted step
    
    Note: Returning fval and g can possibly save on extra computation (why!)
    """
    #Your code here
    alpha = ...
    fval = ...
    g = ...
    return alpha,fval,g

def steepest_descent(x0,f,gradf,c0,c1,t0):
    """Steepest descent with weak Wolfe line bisection search

    Parameters
    ----------
    x0 : initialization
    f : objective function
    gradf : gradient of f
    c0 : Parameter for W1 condition (you may want to set a default)
    c1 : Parameter for W2 condition (you may want to set a default)
    t0 : Initial stepsize for line search
    """
    function_history = ...
    cumulative_times = ...
    gradient_norms = ...
    x_sol = ...
    return x_sol,function_history,cumulative_times,gradient_norms

def DFP(x0,f,gradf,c0,c1,t0):
    """DFP with weak Wolfe line bisection search

    Parameters
    ----------
    x0 : initialization
    f : objective function
    gradf : gradient of f
    c0 : Parameter for W1 condition (you may want to set a default)
    c1 : Parameter for W2 condition (you may want to set a default)
    t0 : Initial stepsize for line search (you may want to set a default)
    """
    function_history = ...
    cumulative_times = ...
    gradient_norms = ...
    x_sol = ...
    return x_sol,function_history,cumulative_times,gradient_norms

def BFGS(x0,f,gradf,c0,c1,t0):
    """BFGS with weak Wolfe line bisection search

    Parameters
    ----------
    x0 : initialization
    f : objective function
    gradf : gradient of f
    c0 : Parameter for W1 condition (you may want to set a default)
    c1 : Parameter for W2 condition (you may want to set a default)
    t0 : Initial stepsize for line search (you may want to set a default)
    """
    function_history = ...
    cumulative_times = ...
    gradient_norms = ...
    x_sol = ...
    return x_sol,function_history,cumulative_times,gradient_norms


def newton(x0,f,gradf,hessf,c0,c1,t0):
    """Newton's method with weak Wolfe line bisection search

    Parameters
    ----------
    x0 : initialization
    f : objective function
    gradf : gradient of f
    hessf : hessian of f
    c0 : Parameter for W1 condition (you may want to set a default)
    c1 : Parameter for W2 condition (you may want to set a default)
    t0 : Initial stepsize for line search (you may want to set a default)
    """
    function_history = ...
    cumulative_times = ...
    gradient_norms = ...
    x_sol = ...
    return x_sol,function_history,cumulative_times,gradient_norms
