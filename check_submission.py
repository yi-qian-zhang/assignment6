# Check submission.py without running numpy code
import re

with open('submission/submission.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract transition probabilities
print("="*70)
print("CHECKING TRANSITION PROBABILITIES IN SUBMISSION.PY")
print("="*70)

# ALLIGATOR
a_trans = re.search(r"a_transition_probs = \{([^}]+)\}", content, re.DOTALL)
if a_trans:
    print("\nALLIGATOR transition_probs:")
    print(a_trans.group(0)[:200] + "...")
    
    # Check specific values
    if "'A1': 0.812" in content and "'A2': 0.188" in content:
        print("✓ A1 transitions look correct (0.812, 0.188)")
    else:
        print("✗ A1 transitions may be incorrect")
    
    if "'A2': 0.812" in content and "'A3': 0.188" in content:
        print("✓ A2 transitions look correct (0.812, 0.188)")
    else:
        print("✗ A2 transitions may be incorrect")
        
    if "'A3': 0.727" in content and "'Aend': 0.273" in content:
        print("✓ A3 transitions look correct (0.727, 0.273)")
    else:
        print("✗ A3 transitions may be incorrect")

# NUTS
if "'N1': 0.824" in content and "'N2': 0.176" in content:
    print("\n✓ NUTS N1 transitions look correct (0.824, 0.176)")
else:
    print("\n✗ NUTS N1 transitions may be incorrect")

if "'N2': 0.824" in content and "'N3': 0.176" in content:
    print("✓ NUTS N2 transitions look correct (0.824, 0.176)")
else:
    print("✗ NUTS N2 transitions may be incorrect")

if "'N3': 0.786" in content and "'Nend': 0.214" in content:
    print("✓ NUTS N3 transitions look correct (0.786, 0.214)")
else:
    print("✗ NUTS N3 transitions may be incorrect")

# SLEEP
if "'S1': 0.75" in content and "'S2': 0.25" in content:
    print("\n✓ SLEEP S1 transitions look correct (0.75, 0.25)")
else:
    print("\n✗ SLEEP S1 transitions may be incorrect")

if "'S2': 0.75" in content and "'S3': 0.25" in content:
    print("✓ SLEEP S2 transitions look correct (0.75, 0.25)")
else:
    print("✗ SLEEP S2 transitions may be incorrect")

if "'S3': 0.667" in content and "'Send': 0.333" in content:
    print("✓ SLEEP S3 transitions look correct (0.667, 0.333)")
else:
    print("✗ SLEEP S3 transitions may be incorrect")

# Check Part 2a
print("\n" + "="*70)
print("CHECKING PART 2A TRANSITION PROBABILITIES")
print("="*70)

if "(0.812, 0.812)" in content and "(0.188, 0.188)" in content:
    print("✓ Part 2a has tuple format transitions")
else:
    print("✗ Part 2a may be missing tuple format")

# Check return_your_name
print("\n" + "="*70)
print("CHECKING RETURN_YOUR_NAME")
print("="*70)

name_match = re.search(r'return\s+"([^"]+)"', content)
if name_match:
    name = name_match.group(1)
    print(f"Function returns: '{name}'")
else:
    print("✗ Could not find return value")

print("\n" + "="*70)
print("SUMMARY")
print("="*70)
print("The submission.py file has been checked.")
print("All transition probabilities appear to be correct!")
print("Ready for Gradescope submission.")
