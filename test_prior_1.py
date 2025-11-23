import numpy as np

evidence = [20, 65, 20, 30, 45, 60, 60, 42]
expected_prob = 5.739096406102214e-17

a_emis_A1 = (51.056, 21.986)

def gaussian_prob(x, para_tuple):
    mean, std = para_tuple
    return (2 * np.pi * std**2)**-0.5 * np.exp(-(x - mean)**2 / (2 * std**2))

emission_product = 1.0
for obs in evidence:
    emission_product *= gaussian_prob(obs, a_emis_A1)

print("If we ignore transitions completely:")
print(f"  prior=1.0, emissions={emission_product:.6e}")
print(f"  Total={emission_product:.6e}")
print(f"  Expected={expected_prob:.6e}")
print(f"  Ratio={emission_product / expected_prob:.6f}")

# Try different combinations
trans_probs = [1.0, 0.764, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.236]
for trans in trans_probs:
    prob = 1.0 * emission_product * (trans**7)
    if abs(prob - expected_prob) / expected_prob < 0.01:
        print(f"\nFOUND: trans={trans}, prob={prob:.6e}, matches expected!")
        
# Find the exact transition probability needed
required_trans = (expected_prob / emission_product) ** (1.0/7.0)
print(f"\nRequired transition probability: {required_trans}")

# Try with prior=0.333
prob_with_033 = 0.333 * emission_product * (required_trans**7)
print(f"With prior=0.333 and trans={required_trans}: {prob_with_033:.6e}")
