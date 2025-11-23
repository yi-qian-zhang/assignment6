import math

# Manual calculation for Part 1a

def mean(vals):
    return sum(vals) / len(vals)

def std(vals):
    m = mean(vals)
    variance = sum((x - m) ** 2 for x in vals) / len(vals)
    return math.sqrt(variance)

def round3(val):
    return round(val, 3)

# ALLIGATOR training data with INITIAL state assignments
alligator_data = [
    {'s1': [31, 28, 28, 37, 68, 49], 's2': [64, 66, 22, 17, 53, 73], 's3': [81, 78, 48, 49, 47]},
    {'s1': [25, 62, 75, 80], 's2': [75, 36, 74, 33], 's3': [27, 34]},
    {'s1': [-4, 69, 59, 45, 62, 22], 's2': [17, 28, 12, 14, 24, 32], 's3': [39, 61, 35, 32]}
]

# NUTS training data with INITIAL state assignments
nuts_data = [
    {'s1': [45, 68, 62, 75], 's2': [61, 44, 73, 72], 's3': [71, 75, 55]},
    {'s1': [33, 33, 32, 32, 34, 38], 's2': [43, 41, 35, 36, 36, 37], 's3': [38, 38, 39, 40, 38, 38]},
    {'s1': [33, 31, 29, 28, 25, 24, 25], 's2': [28, 28, 38, 37, 40, 37, 36], 's3': [36, 38, 44, 48, 48]}
]

# SLEEP training data with INITIAL state assignments
sleep_data = [
    {'s1': [37, 35, 41], 's2': [39, 41, 38], 's3': [38, 38]},
    {'s1': [22, 17, 18, 35], 's2': [33, 36, 42, 36], 's3': [41, 41, 37, 38]},
    {'s1': [38, 37, 35, 32, 35], 's2': [13, 36, 41, 41, 31], 's3': [32, 34, 34]}
]

print("ALLIGATOR - Initial Assignment:")
all_s1 = []
all_s2 = []
all_s3 = []
for d in alligator_data:
    all_s1.extend(d['s1'])
    all_s2.extend(d['s2'])
    all_s3.extend(d['s3'])

print(f"S1: {all_s1}")
print(f"S1 mean: {round3(mean(all_s1))}, std: {round3(std(all_s1))}, count: {len(all_s1)}")
print(f"S2: {all_s2}")
print(f"S2 mean: {round3(mean(all_s2))}, std: {round3(std(all_s2))}, count: {len(all_s2)}")
print(f"S3: {all_s3}")
print(f"S3 mean: {round3(mean(all_s3))}, std: {round3(std(all_s3))}, count: {len(all_s3)}")

# Transition probabilities for ALLIGATOR
# We have 3 sequences, so 3 transitions from S1->S2, 3 from S2->S3, 3 from S3->end
n_seqs = 3
s1_total = len(all_s1)
s2_total = len(all_s2)
s3_total = len(all_s3)

p_s1_s2 = round3(n_seqs / s1_total)
p_s1_s1 = round3(1 - p_s1_s2)

p_s2_s3 = round3(n_seqs / s2_total)
p_s2_s2 = round3(1 - p_s2_s3)

p_s3_end = round3(n_seqs / s3_total)
p_s3_s3 = round3(1 - p_s3_end)

print(f"\nALLIGATOR Transitions:")
print(f"P(A1->A1) = {p_s1_s1}, P(A1->A2) = {p_s1_s2}")
print(f"P(A2->A2) = {p_s2_s2}, P(A2->A3) = {p_s2_s3}")
print(f"P(A3->A3) = {p_s3_s3}, P(A3->end) = {p_s3_end}")

print("\n" + "="*70)
print("NUTS - Initial Assignment:")
all_s1 = []
all_s2 = []
all_s3 = []
for d in nuts_data:
    all_s1.extend(d['s1'])
    all_s2.extend(d['s2'])
    all_s3.extend(d['s3'])

print(f"S1: {all_s1}")
print(f"S1 mean: {round3(mean(all_s1))}, std: {round3(std(all_s1))}, count: {len(all_s1)}")
print(f"S2: {all_s2}")
print(f"S2 mean: {round3(mean(all_s2))}, std: {round3(std(all_s2))}, count: {len(all_s2)}")
print(f"S3: {all_s3}")
print(f"S3 mean: {round3(mean(all_s3))}, std: {round3(std(all_s3))}, count: {len(all_s3)}")

s1_total = len(all_s1)
s2_total = len(all_s2)
s3_total = len(all_s3)

p_s1_s2 = round3(n_seqs / s1_total)
p_s1_s1 = round3(1 - p_s1_s2)

p_s2_s3 = round3(n_seqs / s2_total)
p_s2_s2 = round3(1 - p_s2_s3)

p_s3_end = round3(n_seqs / s3_total)
p_s3_s3 = round3(1 - p_s3_end)

print(f"\nNUTS Transitions:")
print(f"P(N1->N1) = {p_s1_s1}, P(N1->N2) = {p_s1_s2}")
print(f"P(N2->N2) = {p_s2_s2}, P(N2->N3) = {p_s2_s3}")
print(f"P(N3->N3) = {p_s3_s3}, P(N3->end) = {p_s3_end}")

print("\n" + "="*70)
print("SLEEP - Initial Assignment:")
all_s1 = []
all_s2 = []
all_s3 = []
for d in sleep_data:
    all_s1.extend(d['s1'])
    all_s2.extend(d['s2'])
    all_s3.extend(d['s3'])

print(f"S1: {all_s1}")
print(f"S1 mean: {round3(mean(all_s1))}, std: {round3(std(all_s1))}, count: {len(all_s1)}")
print(f"S2: {all_s2}")
print(f"S2 mean: {round3(mean(all_s2))}, std: {round3(std(all_s2))}, count: {len(all_s2)}")
print(f"S3: {all_s3}")
print(f"S3 mean: {round3(mean(all_s3))}, std: {round3(std(all_s3))}, count: {len(all_s3)}")

s1_total = len(all_s1)
s2_total = len(all_s2)
s3_total = len(all_s3)

p_s1_s2 = round3(n_seqs / s1_total)
p_s1_s1 = round3(1 - p_s1_s2)

p_s2_s3 = round3(n_seqs / s2_total)
p_s2_s2 = round3(1 - p_s2_s3)

p_s3_end = round3(n_seqs / s3_total)
p_s3_s3 = round3(1 - p_s3_end)

print(f"\nSLEEP Transitions:")
print(f"P(S1->S1) = {p_s1_s1}, P(S1->S2) = {p_s1_s2}")
print(f"P(S2->S2) = {p_s2_s2}, P(S2->S3) = {p_s2_s3}")
print(f"P(S3->S3) = {p_s3_s3}, P(S3->end) = {p_s3_end}")
