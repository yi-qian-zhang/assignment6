import numpy as np

# Check the expected probability for all-A1 path
evidence = [20, 65, 20, 30, 45, 60, 60, 42]
expected_prob = 5.739096406102214e-17

# Using ALLIGATOR parameters from part_1_a
a_prior = {'A1': 0.333, 'A2': 0.0, 'A3': 0.0, 'Aend': 0.0}
a_trans = {
    'A1': {'A1': 0.236, 'A2': 0.764, 'A3': 0.0, 'Aend': 0.0},
    'A2': {'A1': 0.0, 'A2': 0.338, 'A3': 0.662, 'Aend': 0.0},
    'A3': {'A1': 0.0, 'A2': 0.0, 'A3': 0.213, 'Aend': 0.787},
    'Aend': {'A1': 0.0, 'A2': 0.0, 'A3': 0.0, 'Aend': 1.0}
}
a_emis = {
    'A1': (51.056, 21.986),
    'A2': (28.357, 14.936),
    'A3': (53.727, 16.707),
    'Aend': (None, None)
}

def gaussian_prob(x, para_tuple):
    if list(para_tuple) == [None, None]:
        return 0.0
    mean, std = para_tuple
    gaussian_percentile = (2 * np.pi * std**2)**-0.5 * \
                          np.exp(-(x - mean)**2 / (2 * std**2))
    return gaussian_percentile

# Calculate all-A1 path probability
print("Calculating all-A1 path probability:")
print(f"Evidence: {evidence}")
print(f"A1 emission params: mean={a_emis['A1'][0]}, std={a_emis['A1'][1]}")
print(f"A1 prior: {a_prior['A1']}")
print(f"A1->A1 transition: {a_trans['A1']['A1']}")
print()

prob = a_prior['A1']
print(f"t=0: prob = prior[A1] = {prob}")

for i, obs in enumerate(evidence):
    emission = gaussian_prob(obs, a_emis['A1'])
    prob *= emission
    print(f"t={i}: obs={obs}, emission={emission:.6e}, prob after emission={prob:.6e}")

    if i < len(evidence) - 1:  # Don't multiply by transition after last observation
        prob *= a_trans['A1']['A1']
        print(f"      after transition A1->A1 ({a_trans['A1']['A1']}): prob={prob:.6e}")

print(f"\nFinal probability: {prob:.6e}")
print(f"Expected probability: {expected_prob:.6e}")
print(f"Ratio (calculated / expected): {prob / expected_prob if expected_prob != 0 else 'inf'}")
print()

# What if the prior should be 1.0 for A1?
prob_with_prior_1 = prob / a_prior['A1'] * 1.0
print(f"If prior[A1] = 1.0 instead of 0.333: {prob_with_prior_1:.6e}")
print(f"Ratio to expected: {prob_with_prior_1 / expected_prob}")
