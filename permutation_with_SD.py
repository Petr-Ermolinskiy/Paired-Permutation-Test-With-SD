########
'''
This code is an implamentation of the idea of the dependent data permutation test utilizing the error of measurement. 
Also, these sets of tests are called paired permutation tests.

'''
########
# necessary libraries
import itertools
import numpy as np
########

########
# main function to find the p value using paired permutation tests with standart deviations
########
def permutation_with_SD(x: list, x_sd: list, y: list, y_sd: list, alternative='two-sided'):
    
    error_handling(x, x_sd, y, y_sd)
    
    # all possible combinations of values using standard deviation
    x_combination=combinations_mean_and_sd(x, x_sd)
    y_combination=combinations_mean_and_sd(y, y_sd)
    
    # generate all possible combinations
    all_combinations = list(itertools.product(x_combination, y_combination))
    
    all_mean_combination = []
    # generate all possible combinations with different signs. note that only the increment of values (in percent) is considered. 
    for turple_one_comb in all_combinations:
        one_combination = [j/i*100-100 for i,j in zip(turple_one_comb[0], turple_one_comb[1])]
        for signs in itertools.product([-1, 1], repeat=len(one_combination)):
            combination = Average([number * sign for number, sign in zip(one_combination, signs)])
            all_mean_combination.append(combination)
    # this is the average difference in percent between the second and the first group 
    the_average_betweeen_2_and_1  = Average([j/i*100-100 for i,j in zip(x, y)])
    # calculate the p-value
    if alternative == 'two-sided' or alternative == 't-s':
        p_value = np.sum(np.abs(np.array(all_mean_combination)) < abs(the_average_betweeen_2_and_1)) / len(all_mean_combination)
    elif alternative == 'greater' or alternative == 'g':
        p_value = np.sum(np.array(all_mean_combination) < the_average_betweeen_2_and_1) / len(all_mean_combination)
    elif alternative == 'less' or alternative == 'l':
        p_value = np.sum(np.array(all_mean_combination) > the_average_betweeen_2_and_1) / len(all_mean_combination)
    else:
        raise ValueError('Alternative must be either \"greater\" (\"g\") or \"less\" (\"l\") or \"two-sided\" (\"t-s\")')
    
    print(f'{p_value = }\nTotal number of combinations: {len(all_mean_combination)}')
    print(f'Comparing the second group with the first, the average difference is {the_average_betweeen_2_and_1:.2f}%')
    return (p_value, float(the_average_betweeen_2_and_1), all_mean_combination)


# find the average in the list
def Average(lst): 
    return sum(lst) / len(lst) 

# function to get different combinations of values using mean and sd
# for example, for list x=[5,6] and x_sd=[1,2] the result would be: [[6, 8], [6, 4], [6, 6], [4, 8], [4, 4], [4, 6], [5, 8], [5, 4], [5, 6]]
def combinations_mean_and_sd(massive_mean: list, massive_SD: list):
    # Generate all possible combinations
    combinations = []
    sign_options = [-1, 1, 0]
    for signs in itertools.product(sign_options, repeat=len(massive_mean)):
        combination = [mean + sign * sd for mean, sign, sd in zip(massive_mean, signs, massive_SD)]
        combinations.append(combination)
    return combinations

# error handling
def error_handling(x, x_sd, y, y_sd):
    for i in [x, x_sd, y, y_sd]:
        if type(i) != list:
            raise ValueError(f'The type of {i} must be the list')
    if len(x) == len(y) and len(x_sd) == len(y_sd) and len(x) == len(x_sd):
        pass
    else:
        raise ValueError(f'All lists must have the same length')
    
# plotting a detributions graph to calculate the p-value
def plot_the_distribution(comb_all: list, average: float):
    import matplotlib.pyplot as plt

    plt.hist(comb_all, color='lightgreen', ec='black', bins=20)
    plt.axvline(x = average, color = 'b')
    plt.ylabel('Number')
    plt.xlabel('The average difference in percents between\n the second and the first group (%)')
