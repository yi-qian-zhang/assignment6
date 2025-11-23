import json
import sys

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
try:
    exec('\n\n'.join(code), exec_globals)
    print("[PASS] All code executed successfully")
except Exception as e:
    print(f"[FAIL] Error executing code: {e}")
    sys.exit(1)

# Verify all required functions exist
required_funcs = ['part_1_a', 'viterbi', 'part_2_a', 'multidimensional_viterbi', 'return_your_name', 'gaussian_prob']
for func_name in required_funcs:
    if func_name in exec_globals:
        print(f"[PASS] Function '{func_name}' found")
    else:
        print(f"[FAIL] Function '{func_name}' NOT found")
        sys.exit(1)

# Test return_your_name
return_your_name = exec_globals['return_your_name']
name = return_your_name()
print(f"[PASS] return_your_name() returns: '{name}'")

# Quick test of part_1_a
part_1_a = exec_globals['part_1_a']
result_1a = part_1_a()
print(f"[PASS] part_1_a() returns {len(result_1a)} tuples")

# Quick test of part_2_a
part_2_a = exec_globals['part_2_a']
result_2a = part_2_a()
print(f"[PASS] part_2_a() returns {len(result_2a)} tuples")

# Test viterbi with a simple case
viterbi = exec_globals['viterbi']
(a_prior, a_trans, a_emis, _, _, _, _, _, _) = result_1a
test_evidence = [50, 30, 55]
test_states = ['A1', 'A2', 'A3', 'Aend']
seq, prob = viterbi(test_evidence, test_states, a_prior, a_trans, a_emis)
print(f"[PASS] viterbi() returns sequence of length {len(seq)} with probability {prob:.2e}")

# Test multidimensional_viterbi
multidimensional_viterbi = exec_globals['multidimensional_viterbi']
(a_prior_2, a_trans_2, a_emis_2, _, _, _, _, _, _) = result_2a
test_evidence_2d = [(50, 50), (30, 40), (55, 51)]
seq_2d, prob_2d = multidimensional_viterbi(test_evidence_2d, test_states, a_prior_2, a_trans_2, a_emis_2)
print(f"[PASS] multidimensional_viterbi() returns sequence of length {len(seq_2d)} with probability {prob_2d:.2e}")

print("\n" + "="*70)
print("ALL BASIC TESTS PASSED!")
print("="*70)
print("\nNow you can run the submission tests:")
print("  python notebook2script.py submission")
print("Then submit the generated submission.py file to Gradescope.")
