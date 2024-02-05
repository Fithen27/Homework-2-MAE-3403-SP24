import math
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Find the root of a function using the Secant Method
    :param fcn: The Function to find the root
    :param x0: The first Initial guess
    :param x1: The second initial guess
    :param maxiter: Maximum number of iterations
    :param xtol: Exit if the absolute difference between the consecutive x values is less than xtol
    :return: Float: The final estimate of the root.
    """
    x_prev = x0
    x_curr = x1
    # Code for iteration below was written with help of ChatGPT
    for iteration in range(maxiter):
        f_x_prev = fcn(x_prev)
        f_x_curr = fcn(x_curr)

        # Secant method formula
        x_new = x_curr - f_x_curr * (x_curr - x_prev) / (f_x_curr - f_x_prev)

        # Check for convergence
        if abs(x_new - x_curr) < xtol:
            return x_new

        x_prev, x_curr = x_curr, x_new

    return x_curr

def fcn_1(x):
    """
    First example function for secant method
    :param x: The input value
    :return:THe value of the function at x
    """
    return math.pow(x,3) - math.cos(x)

def fcn_2(x):
    """
    Second example function for secant method
    :param x: The input value
    :return: The value of the function at x
    """
    return 3*math.cos(2*x)

def fcn_3(x):
    """
    Third example fuctnion for secant method
    :param x: The input value
    :return: The values of the function at x
    """
    return 3*x*math.cos(2*x)

def main():
    """
    Main fucntion to demostrate the Secant function.
    :return: Caculations for secant caculations
    """
    # Example 1, calculation using secant method
    result_1 = Secant(fcn_1, 1, 2, maxiter=5, xtol=1e-4)
    print(f'Solution 1: {result_1:.6f}')

    # Example 2, calculation using secant method
    result_2 = Secant(fcn_2, 1, 2, maxiter=15, xtol=1e-8)
    print(f'Solution 2: {result_2:.10f}')

    # Example 3, calculation using secant method
    result_3 = Secant(fcn_3, 1, 2, maxiter=3, xtol=1e-8)
    print(f'Solution 3: {result_3:.10f}')


if __name__ == "__main__":
    main()
