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

# Now we can test
part_1_a = exec_globals['part_1_a']

# Test the function
result = part_1_a()
print("Function executed successfully!")
print("\nResults:")
print("="*70)

# Unpack results
(a_prior, a_trans, a_emis,
 n_prior, n_trans, n_emis,
 s_prior, s_trans, s_emis) = result

print("\nALLIGATOR:")
print(f"Prior: {a_prior}")
print(f"Emission A1: {a_emis['A1']}")
print(f"Emission A2: {a_emis['A2']}")
print(f"Emission A3: {a_emis['A3']}")
print(f"Transition A1: {a_trans['A1']}")
print(f"Transition A2: {a_trans['A2']}")
print(f"Transition A3: {a_trans['A3']}")

print("\nNUTS:")
print(f"Prior: {n_prior}")
print(f"Emission N1: {n_emis['N1']}")
print(f"Emission N2: {n_emis['N2']}")
print(f"Emission N3: {n_emis['N3']}")
print(f"Transition N1: {n_trans['N1']}")
print(f"Transition N2: {n_trans['N2']}")
print(f"Transition N3: {n_trans['N3']}")

print("\nSLEEP:")
print(f"Prior: {s_prior}")
print(f"Emission S1: {s_emis['S1']}")
print(f"Emission S2: {s_emis['S2']}")
print(f"Emission S3: {s_emis['S3']}")
print(f"Transition S1: {s_trans['S1']}")
print(f"Transition S2: {s_trans['S2']}")
print(f"Transition S3: {s_trans['S3']}")
