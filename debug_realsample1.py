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

# Execute the code
exec_globals = {}
exec('\n\n'.join(code), exec_globals)

# Get functions
part_1_a = exec_globals['part_1_a']
gaussian_prob = exec_globals['gaussian_prob']

# Get HMM parameters
a_states = ['A1', 'A2', 'A3', 'Aend']
n_states = ['N1', 'N2', 'N3', 'Nend']
s_states = ['S1', 'S2', 'S3', 'Send']

(a_prior_probs, a_transition_probs, a_emission_paras,
 n_prior_probs, n_transition_probs, n_emission_paras,
 s_prior_probs, s_transition_probs, s_emission_paras) = part_1_a()

states = a_states + n_states + s_states
prior = a_prior_probs
prior.update(n_prior_probs)
prior.update(s_prior_probs)

trans = a_transition_probs
trans.update(n_transition_probs)
trans.update(s_transition_probs)

emiss = a_emission_paras
emiss.update(n_emission_paras)
emiss.update(s_emission_paras)

# Test the failing case
evidence = [20, 65, 20, 30, 45, 60, 60, 42]

print("="*70)
print("Testing observation 20")
print("="*70)
for state in ['A1', 'N1', 'S1']:
    prob = gaussian_prob(20, emiss[state])
    prior_prob = prior.get(state, 0.0)
    total = prior_prob * prob
    print(f"{state}: prior={prior_prob}, emission={prob:.6e}, total={total:.6e}")

print("\n" + "="*70)
print("Manual Viterbi trace for first observation:")
print("="*70)

# t=0
v0 = {}
for state in states:
    prior_prob = prior.get(state, 0.0)
    emission = gaussian_prob(evidence[0], emiss[state])
    v0[state] = prior_prob * emission

# Sort and print top 5
sorted_states = sorted(v0.items(), key=lambda x: x[1], reverse=True)
print(f"\nTop 5 states at t=0 (obs={evidence[0]}):")
for state, prob in sorted_states[:5]:
    print(f"  {state}: {prob:.6e}")

# Check A1 specifically
print(f"\nChecking A1 at each timestep:")
print(f"t=0: V[A1] = {prior['A1']} * {gaussian_prob(evidence[0], emiss['A1']):.6e} = {v0['A1']:.6e}")

# t=1
print(f"\nt=1 (obs={evidence[1]}):")
emission_a1_t1 = gaussian_prob(evidence[1], emiss['A1'])
prob_a1_a1 = v0['A1'] * trans['A1']['A1'] * emission_a1_t1
print(f"  A1->A1: {v0['A1']:.6e} * {trans['A1']['A1']} * {emission_a1_t1:.6e} = {prob_a1_a1:.6e}")

# Now check what the best path is
print("\n" + "="*70)
print("Checking if ALLIGATOR path is actually best:")
print("="*70)

# Calculate probability for all-A1 path
prob_all_a1 = prior['A1'] * gaussian_prob(evidence[0], emiss['A1'])
for t in range(1, len(evidence)):
    prob_all_a1 *= trans['A1']['A1'] * gaussian_prob(evidence[t], emiss['A1'])
print(f"All-A1 path probability: {prob_all_a1:.6e}")

# Calculate probability for current (wrong) path: N1,N1,N1,N1,N1,N1,N1,N2
path = ['N1', 'N1', 'N1', 'N1', 'N1', 'N1', 'N1', 'N2']
prob_path = prior[path[0]] * gaussian_prob(evidence[0], emiss[path[0]])
for t in range(1, len(evidence)):
    prob_path *= trans[path[t-1]][path[t]] * gaussian_prob(evidence[t], emiss[path[t]])
print(f"N1->N1->...->N2 path probability: {prob_path:.6e}")

print(f"\nRatio (A1 path / N path): {prob_all_a1 / prob_path if prob_path != 0 else 'inf'}")
