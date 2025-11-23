import json
import math

def mean(vals):
    return sum(vals) / len(vals)

def std(vals):
    m = mean(vals)
    variance = sum((x - m) ** 2 for x in vals) / len(vals)
    return math.sqrt(variance)

# Initial state assignments
a_s1 = [31, 28, 28, 37, 68, 49, 25, 62, 75, 80, -4, 69, 59, 45, 62, 22]
a_s2 = [64, 66, 22, 17, 53, 73, 75, 36, 74, 33, 17, 28, 12, 14, 24, 32]
a_s3 = [81, 78, 48, 49, 47, 27, 34, 39, 61, 35, 32]

n_s1 = [45, 68, 62, 75, 33, 33, 32, 32, 34, 38, 33, 31, 29, 28, 25, 24, 25]
n_s2 = [61, 44, 73, 72, 43, 41, 35, 36, 36, 37, 28, 28, 38, 37, 40, 37, 36]
n_s3 = [71, 75, 55, 38, 38, 39, 40, 38, 38, 36, 38, 44, 48, 48]

s_s1 = [37, 35, 41, 22, 17, 18, 35, 38, 37, 35, 32, 35]
s_s2 = [39, 41, 38, 33, 36, 42, 36, 13, 36, 41, 41, 31]
s_s3 = [38, 38, 41, 41, 37, 38, 32, 34, 34]

# Calculate parameters
n_seqs = 3

# ALLIGATOR
a1_mean, a1_std = round(mean(a_s1), 3), round(std(a_s1), 3)
a2_mean, a2_std = round(mean(a_s2), 3), round(std(a_s2), 3)
a3_mean, a3_std = round(mean(a_s3), 3), round(std(a_s3), 3)

a1_s1 = round(1 - n_seqs / len(a_s1), 3)
a1_s2 = round(n_seqs / len(a_s1), 3)
a2_s2 = round(1 - n_seqs / len(a_s2), 3)
a2_s3 = round(n_seqs / len(a_s2), 3)
a3_s3 = round(1 - n_seqs / len(a_s3), 3)
a3_end = round(n_seqs / len(a_s3), 3)

# NUTS  
n1_mean, n1_std = round(mean(n_s1), 3), round(std(n_s1), 3)
n2_mean, n2_std = round(mean(n_s2), 3), round(std(n_s2), 3)
n3_mean, n3_std = round(mean(n_s3), 3), round(std(n_s3), 3)

n1_s1 = round(1 - n_seqs / len(n_s1), 3)
n1_s2 = round(n_seqs / len(n_s1), 3)
n2_s2 = round(1 - n_seqs / len(n_s2), 3)
n2_s3 = round(n_seqs / len(n_s2), 3)
n3_s3 = round(1 - n_seqs / len(n_s3), 3)
n3_end = round(n_seqs / len(n_s3), 3)

# SLEEP
s1_mean, s1_std = round(mean(s_s1), 3), round(std(s_s1), 3)
s2_mean, s2_std = round(mean(s_s2), 3), round(std(s_s2), 3)
s3_mean, s3_std = round(mean(s_s3), 3), round(std(s_s3), 3)

s1_s1 = round(1 - n_seqs / len(s_s1), 3)
s1_s2 = round(n_seqs / len(s_s1), 3)
s2_s2 = round(1 - n_seqs / len(s_s2), 3)
s2_s3 = round(n_seqs / len(s_s2), 3)
s3_s3 = round(1 - n_seqs / len(s_s3), 3)
s3_end = round(n_seqs / len(s_s3), 3)

print("ALLIGATOR:")
print(f"  A1: mean={a1_mean}, std={a1_std}")
print(f"  A2: mean={a2_mean}, std={a2_std}")
print(f"  A3: mean={a3_mean}, std={a3_std}")
print(f"  A1->A1={a1_s1}, A1->A2={a1_s2}")
print(f"  A2->A2={a2_s2}, A2->A3={a2_s3}")
print(f"  A3->A3={a3_s3}, A3->Aend={a3_end}")

print("\nNUTS:")
print(f"  N1: mean={n1_mean}, std={n1_std}")
print(f"  N2: mean={n2_mean}, std={n2_std}")
print(f"  N3: mean={n3_mean}, std={n3_std}")
print(f"  N1->N1={n1_s1}, N1->N2={n1_s2}")
print(f"  N2->N2={n2_s2}, N2->N3={n2_s3}")
print(f"  N3->N3={n3_s3}, N3->Nend={n3_end}")

print("\nSLEEP:")
print(f"  S1: mean={s1_mean}, std={s1_std}")
print(f"  S2: mean={s2_mean}, std={s2_std}")
print(f"  S3: mean={s3_mean}, std={s3_std}")
print(f"  S1->S1={s1_s1}, S1->S2={s1_s2}")
print(f"  S2->S2={s2_s2}, S2->S3={s2_s3}")
print(f"  S3->S3={s3_s3}, S3->Send={s3_end}")
