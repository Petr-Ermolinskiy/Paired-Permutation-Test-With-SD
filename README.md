
# Paired permutation test utilizing the error of each measurement/value

This repository introduces an extended permutation test for dependent data with small sample sizes,
incorporating measurement errors. This method is especially applicable in single case studies,
offering a valuable tool for hypothesis testing without strict distributional assumptions. Additional
research is needed to fully assess the effectiveness and validity of this approach.

__Note__: this extension of the paired permutation statistical test is under study and its limitations are not yet known. The use of this test should not be accepted when calculating statistical significance in scientific research before this test has been validated. 




## Usage/Examples

An example of usage can be found in the __example.ipynb__ file. 

```python
from permutation_with_SD import permutation_with_SD

# first group - before treatment
x = [20, 33, 20, 24]
# SD of a parameter for the first group
x_sd = [2, 2, 2, 2]

# second group - after treatment
y = [21, 34, 22, 25]
# SD of a parameter for the second group
y_sd = [2, 2, 2, 2]

# p = calculate p-value; 
# average = the average difference in paramenter (%) comparing the first and the second group; 
# comb_all = the massive of all possible average differences calculted using permutations
p, average, comb_all = permutation_with_SD(x, x_sd, y, y_sd, alternative='less')

```


## If it is usufull

If it usufull you can cite this repository, or the preprint in [hal](https://hal.science/hal-04558513):

```bash
Petr Ermolinskiy. An Extension of the Permutation Test for Dependent Data in Samples with a Small Number of Subjects. 2024.
⟨hal-04558513⟩
```
