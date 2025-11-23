import json

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
viterbi = exec_globals['viterbi']

# Get HMM parameters - combining all words
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
prob_ans = 5.739096406102214e-17
seq_ans = ['A1', 'A1', 'A1', 'A1', 'A1', 'A1', 'A1', 'A1']

print(f"Testing Viterbi on realsample1: {evidence}")
seq, prob = viterbi(evidence, states, prior, trans, emiss)
print(f"Result sequence: {seq}")
print(f"Result probability: {prob}")
print(f"Expected sequence: {seq_ans}")
print(f"Expected probability: {prob_ans}")
print(f"Sequence match: {seq == seq_ans}")
print(f"Probability ratio: {prob / prob_ans if prob_ans != 0 else 'N/A'}")
print(f"Probability difference: {abs(prob - prob_ans)}")
print(f"Match to 21 places: {abs(prob - prob_ans) < 1e-21}")
