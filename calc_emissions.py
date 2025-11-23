import math

def mean(vals):
    return sum(vals) / len(vals)

def std(vals):
    m = mean(vals)
    variance = sum((x - m) ** 2 for x in vals) / len(vals)
    return math.sqrt(variance)

# ALLIGATOR
a_s1 = [31, 28, 28, 37, 68, 49, 25, 62, 75, 80, -4, 69, 59, 45, 62, 22]
a_s2 = [64, 66, 22, 17, 53, 73, 75, 36, 74, 33, 17, 28, 12, 14, 24, 32]
a_s3 = [81, 78, 48, 49, 47, 27, 34, 39, 61, 35, 32]

print("ALLIGATOR emissions:")
print(f"  A1: mean={round(mean(a_s1), 3)}, std={round(std(a_s1), 3)}")
print(f"  A2: mean={round(mean(a_s2), 3)}, std={round(std(a_s2), 3)}")
print(f"  A3: mean={round(mean(a_s3), 3)}, std={round(std(a_s3), 3)}")

# NUTS
n_s1 = [45, 68, 62, 75, 33, 33, 32, 32, 34, 38, 33, 31, 29, 28, 25, 24, 25]
n_s2 = [61, 44, 73, 72, 43, 41, 35, 36, 36, 37, 28, 28, 38, 37, 40, 37, 36]
n_s3 = [71, 75, 55, 38, 38, 39, 40, 38, 38, 36, 38, 44, 48, 48]

print("\nNUTS emissions:")
print(f"  N1: mean={round(mean(n_s1), 3)}, std={round(std(n_s1), 3)}")
print(f"  N2: mean={round(mean(n_s2), 3)}, std={round(std(n_s2), 3)}")
print(f"  N3: mean={round(mean(n_s3), 3)}, std={round(std(n_s3), 3)}")

# SLEEP
s_s1 = [37, 35, 41, 22, 17, 18, 35, 38, 37, 35, 32, 35]
s_s2 = [39, 41, 38, 33, 36, 42, 36, 13, 36, 41, 41, 31]
s_s3 = [38, 38, 41, 41, 37, 38, 32, 34, 34]

print("\nSLEEP emissions:")
print(f"  S1: mean={round(mean(s_s1), 3)}, std={round(std(s_s1), 3)}")
print(f"  S2: mean={round(mean(s_s2), 3)}, std={round(std(s_s2), 3)}")
print(f"  S3: mean={round(mean(s_s3), 3)}, std={round(std(s_s3), 3)}")
