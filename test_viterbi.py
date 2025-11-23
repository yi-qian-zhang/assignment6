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
            # Remove #export line and test lines
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

# Get HMM parameters
(a_prior, a_trans, a_emis,
 n_prior, n_trans, n_emis,
 s_prior, s_trans, s_emis) = part_1_a()

# Test on a simple sequence - one of the training sequences for SLEEP
evidence = [38, 37, 35, 32, 35, 13, 36, 41, 41, 31, 32, 34, 34]
states = ['S1', 'S2', 'S3', 'Send']

print(f"Testing Viterbi on SLEEP sequence: {evidence}")
sequence, prob = viterbi(evidence, states, s_prior, s_trans, s_emis)
print(f"Result sequence: {sequence}")
print(f"Probability: {prob}")
print(f"Sequence length: {len(sequence)}, Evidence length: {len(evidence)}")

# Test on ALLIGATOR
evidence_a = [31, 28, 28, 37, 68, 49, 64, 66, 22, 17, 53, 73, 81, 78, 48, 49, 47]
states_a = ['A1', 'A2', 'A3', 'Aend']
print(f"\nTesting Viterbi on ALLIGATOR sequence: {evidence_a}")
sequence_a, prob_a = viterbi(evidence_a, states_a, a_prior, a_trans, a_emis)
print(f"Result sequence: {sequence_a}")
print(f"Probability: {prob_a}")
