import json
import numpy as np

# Load and execute current part_1_a
with open('notebook.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

code = []
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if source.startswith('#export'):
            lines = source.split('\n')
            filtered_lines = [line for line in lines[1:] if 'DON\'T WRITE ANY CODE OUTSIDE THE FUNCTION' not in line]
            code.append('\n'.join(filtered_lines))

exec_globals = {}
exec('\n\n'.join(code), exec_globals)
part_1_a = exec_globals['part_1_a']
gaussian_prob = exec_globals['gaussian_prob']

# Get current parameters
result = part_1_a()
(a_prior, a_trans, a_emis, n_prior, n_trans, n_emis, s_prior, s_trans, s_emis) = result

print("Current ALLIGATOR parameters:")
print(f"  A1->A1 transition: {a_trans['A1']['A1']}")
print(f"  A1->A2 transition: {a_trans['A1']['A2']}")
print(f"  A1 emission: {a_emis['A1']}")

# Calculate what the all-A1 path probability should be for test case
evidence = [20, 65, 20, 30, 45, 60, 60, 42]
prob = a_prior['A1']
for i, obs in enumerate(evidence):
    emission = gaussian_prob(obs, a_emis['A1'])
    prob *= emission
    if i < len(evidence) - 1:
        prob *= a_trans['A1']['A1']

print(f"\nAll-A1 path probability with current params: {prob:.6e}")
print(f"Expected by test: 5.739096406102214e-17")
print(f"Ratio: {prob / 5.739096406102214e-17:.6f}")

# The issue: transition probabilities are too low!
# They should NOT have been adjusted during HMM training
# because the instructions say to use the INITIAL state assignments
