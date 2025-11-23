import json
import numpy as np

# Load notebook
with open('notebook.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

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
viterbi = exec_globals['viterbi']
gaussian_prob = exec_globals['gaussian_prob']

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

# Test case 2 (passing)
evidence = [30]
prob_ans = 0.01576664562875057
seq_ans = ['S1']

seq, prob = viterbi(evidence, states, prior, trans, emiss)
print("Test case 2 (single observation [30]):")
print(f"  Expected: seq={seq_ans}, prob={prob_ans}")
print(f"  Got:      seq={seq}, prob={prob}")
print(f"  Match: {seq == seq_ans and abs(prob - prob_ans) < 1e-7}")

# Manual calculation
print("\n  Manual calculation:")
print(f"    Prior[S1] = {prior['S1']}")
print(f"    Emission(30|S1) = {gaussian_prob(30, emiss['S1']):.6e}")
print(f"    Product = {prior['S1'] * gaussian_prob(30, emiss['S1']):.6e}")

# Check other words
for word_state in ['A1', 'N1']:
    p = prior[word_state] * gaussian_prob(30, emiss[word_state])
    print(f"    {word_state}: {p:.6e}")

print("\n" + "="*70)

# Test case 3 (passing)
evidence = [40]
prob_ans = 0.011713950611283535
seq_ans = ['N1']

seq, prob = viterbi(evidence, states, prior, trans, emiss)
print("Test case 3 (single observation [40]):")
print(f"  Expected: seq={seq_ans}, prob={prob_ans}")
print(f"  Got:      seq={seq}, prob={prob}")
print(f"  Match: {seq == seq_ans and abs(prob - prob_ans) < 1e-7}")

print("\n  Manual calculation:")
print(f"    Prior[N1] = {prior['N1']}")
print(f"    Emission(40|N1) = {gaussian_prob(40, emiss['N1']):.6e}")
print(f"    Product = {prior['N1'] * gaussian_prob(40, emiss['N1']):.6e}")

for word_state in ['A1', 'S1']:
    p = prior[word_state] * gaussian_prob(40, emiss[word_state])
    print(f"    {word_state}: {p:.6e}")
