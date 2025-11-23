import math

def mean(vals):
    return sum(vals) / len(vals)

def std(vals):
    m = mean(vals)
    variance = sum((x - m) ** 2 for x in vals) / len(vals)
    return math.sqrt(variance)

def num_std_away(obs, mean, std):
    if std == 0:
        return float('inf') if obs != mean else 0
    return abs(obs - mean) / std

# ALLIGATOR initial assignments
sequences = [
    {'s1': [31, 28, 28, 37, 68, 49], 's2': [64, 66, 22, 17, 53, 73], 's3': [81, 78, 48, 49, 47]},
    {'s1': [25, 62, 75, 80], 's2': [75, 36, 74, 33], 's3': [27, 34]},
    {'s1': [-4, 69, 59, 45, 62, 22], 's2': [17, 28, 12, 14, 24, 32], 's3': [39, 61, 35, 32]}
]

# Calculate initial parameters
all_s1 = []
all_s2 = []
all_s3 = []
for seq in sequences:
    all_s1.extend(seq['s1'])
    all_s2.extend(seq['s2'])
    all_s3.extend(seq['s3'])

params = [
    (round(mean(all_s1), 3), round(std(all_s1), 3)),
    (round(mean(all_s2), 3), round(std(all_s2), 3)),
    (round(mean(all_s3), 3), round(std(all_s3), 3))
]

print("Initial parameters:")
print(f"S1: mean={params[0][0]}, std={params[0][1]}")
print(f"S2: mean={params[1][0]}, std={params[1][1]}")
print(f"S3: mean={params[2][0]}, std={params[2][1]}")

# Now do ONE iteration of boundary adjustment
print("\nDoing ONE iteration of training...")

full_sequences = [
    [31, 28, 28, 37, 68, 49, 64, 66, 22, 17, 53, 73, 81, 78, 48, 49, 47],
    [25, 62, 75, 80, 75, 36, 74, 33, 27, 34],
    [-4, 69, 59, 45, 62, 22, 17, 28, 12, 14, 24, 32, 39, 61, 35, 32]
]

new_s1 = []
new_s2 = []
new_s3 = []

for seq in full_sequences:
    n = len(seq)
    # Start with equal division
    idx1 = n // 3
    idx2 = 2 * n // 3
    
    s1 = seq[:idx1]
    s2 = seq[idx1:idx2]
    s3 = seq[idx2:]
    
    # Adjust S1-S2 boundary
    while len(s1) > 1:
        left_elem = s1[-1]
        dist_s1 = num_std_away(left_elem, params[0][0], params[0][1])
        dist_s2 = num_std_away(left_elem, params[1][0], params[1][1])
        
        if dist_s2 < dist_s1:
            s2 = [left_elem] + s2
            s1 = s1[:-1]
        else:
            break
    
    while len(s2) > 1:
        right_elem = s2[0]
        dist_s1 = num_std_away(right_elem, params[0][0], params[0][1])
        dist_s2 = num_std_away(right_elem, params[1][0], params[1][1])
        
        if dist_s1 < dist_s2:
            s1 = s1 + [right_elem]
            s2 = s2[1:]
        else:
            break
    
    # Adjust S2-S3 boundary
    while len(s2) > 1:
        left_elem = s2[-1]
        dist_s2 = num_std_away(left_elem, params[1][0], params[1][1])
        dist_s3 = num_std_away(left_elem, params[2][0], params[2][1])
        
        if dist_s3 < dist_s2:
            s3 = [left_elem] + s3
            s2 = s2[:-1]
        else:
            break
    
    while len(s3) > 1:
        right_elem = s3[0]
        dist_s2 = num_std_away(right_elem, params[1][0], params[1][1])
        dist_s3 = num_std_away(right_elem, params[2][0], params[2][1])
        
        if dist_s2 < dist_s3:
            s2 = s2 + [right_elem]
            s3 = s3[1:]
        else:
            break
    
    print(f"\nSequence {len(new_s1)//3 + 1}:")
    print(f"  S1: {s1}")
    print(f"  S2: {s2}")
    print(f"  S3: {s3}")
    
    new_s1.extend(s1)
    new_s2.extend(s2)
    new_s3.extend(s3)

# Calculate new parameters
new_params = [
    (round(mean(new_s1), 3), round(std(new_s1), 3)),
    (round(mean(new_s2), 3), round(std(new_s2), 3)),
    (round(mean(new_s3), 3), round(std(new_s3), 3))
]

print("\nAfter ONE iteration:")
print(f"S1: mean={new_params[0][0]}, std={new_params[0][1]}, count={len(new_s1)}")
print(f"S2: mean={new_params[1][0]}, std={new_params[1][1]}, count={len(new_s2)}")
print(f"S3: mean={new_params[2][0]}, std={new_params[2][1]}, count={len(new_s3)}")

# Calculate transition probabilities
n_seqs = 3
p_s1_s2 = round(n_seqs / len(new_s1), 3)
p_s1_s1 = round(1 - p_s1_s2, 3)
p_s2_s3 = round(n_seqs / len(new_s2), 3)
p_s2_s2 = round(1 - p_s2_s3, 3)
p_s3_end = round(n_seqs / len(new_s3), 3)
p_s3_s3 = round(1 - p_s3_end, 3)

print(f"\nTransition probabilities:")
print(f"A1->A1: {p_s1_s1}, A1->A2: {p_s1_s2}")
print(f"A2->A2: {p_s2_s2}, A2->A3: {p_s2_s3}")
print(f"A3->A3: {p_s3_s3}, A3->Aend: {p_s3_end}")
