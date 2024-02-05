import math

def Probability(PDF, args, c, GT=True):

    """
    Caclulate the probability using Simpsons 1/3 Rule.

    Parameter:  PDF - A callback function for the guassian/normal probability density function. Takes a single argument as
                  a tuple which contains values for x, mu and sigma.
            args - A tuple containing mu and sigma
            c (float) - The upper limit of integration
            GT (bool) - Indicates if we want the probability of x greater than c (GT=True) or less than c (GT=False_)
    returns: Float - The caculated probability
    """
    # Define the limits of integration
    mu, sigma = args
    lower_limit = mu - 5 * sigma
    upper_limit = c

    # Calculate the step size for Simpson's 1/3 rule
    step_size = (upper_limit - lower_limit) / 1000

    # Calculate probabilities using Simpson's 1/3 rule
    probabilities = 0
    for i in range(0, 1000, 2):
        x_midpoint = lower_limit + i * step_size
        probabilities += PDF((x_midpoint, mu, sigma)) * step_size

    # Multiply by 1/3 for Simpson's 1/3 rule
    probabilities *= 1 / 3

    # For P(x>c), subtract from 1 if GT=False
    if not GT:
        probabilities = 1 - probabilities

    return probabilities


def normal_PDF(args):

    """
    Caclulate the nromal probability desnity function
    :param args: A tuple containing x, my, sigma
    :return: Float: The caclulated probability of desnsity
    """
    x, mu, sigma = args
    return 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu) ** 2 / (2 * sigma ** 2))


def main():
    """
    Main Function to desmostrate the probability function
    :return: Displays the probabiility of the two results
    """

    # Example 1: P(x<105|N(100,12.5))
    result_1 = Probability(normal_PDF, (100, 12.5), 105, GT=True)
    print(f'P(x<105|N(100,12.5))={result_1:.2f}')

    # Example 2: P(x>μ+2σ|N(100, 3))
    result_2 = Probability(normal_PDF, (100, 3), 100 + 2 * 3, GT=False)
    print(f'P(x>{100 + 2 * 3}|N(100,3))={result_2:.2f}')


if __name__ == "__main__":
    main()
