# Calculate correct transition probabilities

# ALLIGATOR: S1 has 16 observations, S2 has 18, S3 has 11
# 3 sequences, so 3 exits from each state
a_s1_total = 16
a_s2_total = 18
a_s3_total = 11
n_seqs = 3

a_p_s1_s2 = round(n_seqs / a_s1_total, 3)
a_p_s1_s1 = round(1 - a_p_s1_s2, 3)

a_p_s2_s3 = round(n_seqs / a_s2_total, 3)
a_p_s2_s2 = round(1 - a_p_s2_s3, 3)

a_p_s3_end = round(n_seqs / a_s3_total, 3)
a_p_s3_s3 = round(1 - a_p_s3_end, 3)

print("ALLIGATOR:")
print(f"  A1->A1: {a_p_s1_s1}, A1->A2: {a_p_s1_s2}")
print(f"  A2->A2: {a_p_s2_s2}, A2->A3: {a_p_s2_s3}")
print(f"  A3->A3: {a_p_s3_s3}, A3->Aend: {a_p_s3_end}")

# NUTS: S1 has 17 observations, S2 has 17, S3 has 14
n_s1_total = 17
n_s2_total = 17
n_s3_total = 14

n_p_s1_s2 = round(n_seqs / n_s1_total, 3)
n_p_s1_s1 = round(1 - n_p_s1_s2, 3)

n_p_s2_s3 = round(n_seqs / n_s2_total, 3)
n_p_s2_s2 = round(1 - n_p_s2_s3, 3)

n_p_s3_end = round(n_seqs / n_s3_total, 3)
n_p_s3_s3 = round(1 - n_p_s3_end, 3)

print("\nNUTS:")
print(f"  N1->N1: {n_p_s1_s1}, N1->N2: {n_p_s1_s2}")
print(f"  N2->N2: {n_p_s2_s2}, N2->N3: {n_p_s2_s3}")
print(f"  N3->N3: {n_p_s3_s3}, N3->Nend: {n_p_s3_end}")

# SLEEP: S1 has 12 observations, S2 has 12, S3 has 9
s_s1_total = 12
s_s2_total = 12
s_s3_total = 9

s_p_s1_s2 = round(n_seqs / s_s1_total, 3)
s_p_s1_s1 = round(1 - s_p_s1_s2, 3)

s_p_s2_s3 = round(n_seqs / s_s2_total, 3)
s_p_s2_s2 = round(1 - s_p_s2_s3, 3)

s_p_s3_end = round(n_seqs / s_s3_total, 3)
s_p_s3_s3 = round(1 - s_p_s3_end, 3)

print("\nSLEEP:")
print(f"  S1->S1: {s_p_s1_s1}, S1->S2: {s_p_s1_s2}")
print(f"  S2->S2: {s_p_s2_s2}, S2->S3: {s_p_s2_s3}")
print(f"  S3->S3: {s_p_s3_s3}, S3->Send: {s_p_s3_end}")
