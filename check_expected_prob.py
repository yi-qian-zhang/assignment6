import numpy as np

evidence = [20, 65, 20, 30, 45, 60, 60, 42]
expected_prob = 5.739096406102214e-17

a_prior_A1 = 0.333
a_trans_A1_A1 = 0.236
a_emis_A1 = (51.056, 21.986)

def gaussian_prob(x, para_tuple):
    mean, std = para_tuple
    return (2 * np.pi * std**2)**-0.5 * np.exp(-(x - mean)**2 / (2 * std**2))

emission_product = 1.0
for obs in evidence:
    emission_product *= gaussian_prob(obs, a_emis_A1)
    
print(f'Product of emissions: {emission_product:.6e}')
print(f'Transition prob^7: {a_trans_A1_A1**7:.6e}')
print(f'Prior: {a_prior_A1}')
print(f'Product of all: {a_prior_A1 * emission_product * (a_trans_A1_A1**7):.6e}')
print(f'Expected: {expected_prob:.6e}')
print()

required_coeff = expected_prob / emission_product
print(f'Required (prior * trans^7): {required_coeff:.6e}')
print(f'Current (prior * trans^7): {a_prior_A1 * (a_trans_A1_A1**7):.6e}')
print(f'Ratio: {required_coeff / (a_prior_A1 * (a_trans_A1_A1**7)):.6f}')
