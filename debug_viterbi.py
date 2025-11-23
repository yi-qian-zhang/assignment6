import json
import numpy as np

# Load notebook and extract code
with open('notebook.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Extract all cells with #export
code = []
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if source.startswith('#export'):
            lines = source.split('\n')
            filtered_lines = []
            skip = False
            for line in lines[1:]:
                if 'DON\'T WRITE ANY CODE OUTSIDE THE FUNCTION' in line:
                    skip = True
                if not skip:
                    filtered_lines.append(line)
            code.append('\n'.join(filtered_lines))

exec_globals = {}
exec('\n\n'.join(code), exec_globals)

part_1_a = exec_globals['part_1_a']
gaussian_prob = exec_globals['gaussian_prob']

(a_prior, a_trans, a_emis,
 n_prior, n_trans, n_emis,
 s_prior, s_trans, s_emis) = part_1_a()

# Debug: check emission probabilities for specific observations
print("Testing SLEEP emission probabilities:")
print(f"S1 params: {s_emis['S1']}")
print(f"S2 params: {s_emis['S2']}")
print(f"S3 params: {s_emis['S3']}")

test_obs = [38, 35, 41]
for obs in test_obs:
    print(f"\nObservation: {obs}")
    for state in ['S1', 'S2', 'S3']:
        prob = gaussian_prob(obs, s_emis[state])
        print(f"  P({obs}|{state}) = {prob:.6e}")

# Check transition probabilities
print(f"\nTransition probabilities for SLEEP:")
for state in ['S1', 'S2', 'S3']:
    print(f"{state}: {s_trans[state]}")

# Manual Viterbi trace for first few steps
print("\n" + "="*70)
print("Manual Viterbi trace for sequence [38, 37, 35]:")
evidence = [38, 37, 35]

# t=0
print("\nt=0, observation=38:")
for state in ['S1', 'S2', 'S3']:
    prior = s_prior[state]
    emission = gaussian_prob(38, s_emis[state])
    prob = prior * emission
    print(f"  V[0][{state}] = {prior} * {emission:.6e} = {prob:.6e}")

# t=1
print("\nt=1, observation=37:")
print("  From S1:")
for next_state in ['S1', 'S2', 'S3']:
    trans = s_trans['S1'][next_state]
    emission = gaussian_prob(37, s_emis[next_state])
    # Assuming V[0][S1] from above
    v_prev = s_prior['S1'] * gaussian_prob(38, s_emis['S1'])
    prob = v_prev * trans * emission
    print(f"    V[1][{next_state}] via S1 = {v_prev:.6e} * {trans} * {emission:.6e} = {prob:.6e}")
