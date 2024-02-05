import numpy as np

# Defining the function GaussSeidel, code below written with help of ChatGPT
def GaussSeidel(Aug, x, Niter=15):
    """
    Solve a system of linear equations using the Guass-Seidel Method.
    :param Aug: A augmented matrix containing [A,B], having N rows and N=1 Colums.
    :param x: A vector containing the initial guesses
    :param Niter:The number of iterations to compute
    :return: The final X vector
    """
    # Getting the shape of Aug
    (m, n) = Aug.shape

    # Initialising x0
    x0 = np.empty(shape=n - 1)

    for i in range(n - 1):
        x0[i] = x[i]

    # Getting the matrix a and b from Aug
    a = Aug[:m, :n - 1]
    b = Aug[:m, n - 1].reshape(m)

    # Defining new value of n
    (m, n) = a.shape

    # Initialising the solution
    x = np.zeros(shape=n)

    # Initialising the iteration number
    k = 1

    while k <= Niter:
        for i in range(n):
            s = 0
            for j in range(i):
                if i == j:
                    continue
                else:
                    s += a[i][j] * x[j]
            for j in range(i + 1, n):
                if i == j:
                    continue
                else:
                    s += a[i][j] * x0[j]
            x[i] = (-s + b[i]) / a[i][i]

        # Updating the number of iterations
        k += 1

        # Updating the parameters
        for i in range(n):
            x0[i] = x[i]

    # Returning the solution
    return x


# Writing the main function
if __name__ == "__main__":
    # Part (i)
    # Defining the Aug matrix
    Aug_i = np.array([[3, 1, -1, 2], [1, 4, 1, 12], [2, 1, 2, 10]])

    # Defining initial x
    x_i = np.zeros(shape=Aug_i.shape[0])

    # Calling the function
    x_i = GaussSeidel(Aug_i, x_i)

    # Displaying the solution
    print("Solution of Part (i) is ")
    print(x_i)

    # Part (ii)
    # Defining the Aug matrix
    Aug_ii = np.array([[1, -10, 2, 4, 2], [3, 1, 4, 12, 12], [9, 2, 3, 4, 21], [-1, 2, 7, 3, 37]])

    # Defining initial x
    x_ii = np.zeros(shape=Aug_ii.shape[0])

    # Calling the function
    x_ii = GaussSeidel(Aug_ii, x_ii)

    # Displaying the solution
    print("\nSolution of Part (ii) is ")
    print(x_ii)
