import numpy as np
from scipy.stats import binom

#Probability of getting successs (getting a D)
p_d = (1/5)

#number of successes required
no_of_suc = 5

#number of trials
no_of_trials = 50

p_a_5 = binom.pmf(no_of_suc, no_of_trials, p_a)

'Probability of getting exactly 5 D {0:.7f}'.format(p_a_5)