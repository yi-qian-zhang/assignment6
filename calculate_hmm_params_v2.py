import numpy as np

# Training data with initial state assignments
training_data = {
    'ALLIGATOR': [
        {
            'sequence': [31, 28, 28, 37, 68, 49, 64, 66, 22, 17, 53, 73, 81, 78, 48, 49, 47],
            'initial_s1': [31, 28, 28, 37, 68, 49],
            'initial_s2': [64, 66, 22, 17, 53, 73],
            'initial_s3': [81, 78, 48, 49, 47]
        },
        {
            'sequence': [25, 62, 75, 80, 75, 36, 74, 33, 27, 34],
            'initial_s1': [25, 62, 75, 80],
            'initial_s2': [75, 36, 74, 33],
            'initial_s3': [27, 34]
        },
        {
            'sequence': [-4, 69, 59, 45, 62, 22, 17, 28, 12, 14, 24, 32, 39, 61, 35, 32],
            'initial_s1': [-4, 69, 59, 45, 62, 22],
            'initial_s2': [17, 28, 12, 14, 24, 32],
            'initial_s3': [39, 61, 35, 32]
        }
    ],
    'NUTS': [
        {
            'sequence': [45, 68, 62, 75, 61, 44, 73, 72, 71, 75, 55],
            'initial_s1': [45, 68, 62, 75],
            'initial_s2': [61, 44, 73, 72],
            'initial_s3': [71, 75, 55]
        },
        {
            'sequence': [33, 33, 32, 32, 34, 38, 43, 41, 35, 36, 36, 37, 38, 38, 39, 40, 38, 38],
            'initial_s1': [33, 33, 32, 32, 34, 38],
            'initial_s2': [43, 41, 35, 36, 36, 37],
            'initial_s3': [38, 38, 39, 40, 38, 38]
        },
        {
            'sequence': [33, 31, 29, 28, 25, 24, 25, 28, 28, 38, 37, 40, 37, 36, 36, 38, 44, 48, 48],
            'initial_s1': [33, 31, 29, 28, 25, 24, 25],
            'initial_s2': [28, 28, 38, 37, 40, 37, 36],
            'initial_s3': [36, 38, 44, 48, 48]
        }
    ],
    'SLEEP': [
        {
            'sequence': [37, 35, 41, 39, 41, 38, 38, 38],
            'initial_s1': [37, 35, 41],
            'initial_s2': [39, 41, 38],
            'initial_s3': [38, 38]
        },
        {
            'sequence': [22, 17, 18, 35, 33, 36, 42, 36, 41, 41, 37, 38],
            'initial_s1': [22, 17, 18, 35],
            'initial_s2': [33, 36, 42, 36],
            'initial_s3': [41, 41, 37, 38]
        },
        {
            'sequence': [38, 37, 35, 32, 35, 13, 36, 41, 41, 31, 32, 34, 34],
            'initial_s1': [38, 37, 35, 32, 35],
            'initial_s2': [13, 36, 41, 41, 31],
            'initial_s3': [32, 34, 34]
        }
    ]
}

def calculate_mean_std(values):
    """Calculate mean and standard deviation, rounded to 3 decimals"""
    if not values:
        return 0.0, 0.0
    mean = np.mean(values)
    std = np.std(values, ddof=0)  # Population std
    return round(mean, 3), round(std, 3)

def num_std_away(observation, mean, std):
    """Calculate how many standard deviations away an observation is from the mean"""
    if std == 0:
        return float('inf') if observation != mean else 0
    return abs(observation - mean) / std

def train_hmm(word_name, data_list):
    """Train HMM using the method from Udacity Lesson 8-29"""
    print(f"\n{'='*70}")
    print(f"Training HMM for {word_name}")
    print(f"{'='*70}")

    # Start with initial state assignments
    states = [[], [], []]
    for data in data_list:
        states[0].extend(data['initial_s1'])
        states[1].extend(data['initial_s2'])
        states[2].extend(data['initial_s3'])

    # Calculate initial parameters
    params = [calculate_mean_std(states[i]) for i in range(3)]
    print(f"\nInitial parameters:")
    for i in range(3):
        print(f"  State {i+1}: mean={params[i][0]}, std={params[i][1]}, count={len(states[i])}")

    # Iterative training
    max_iterations = 20
    for iteration in range(max_iterations):
        changed = False

        # Process each training sequence
        new_states = [[], [], []]
        for data in data_list:
            seq = data['sequence']
            # Start with equal division
            n = len(seq)
            # Roughly equal division
            idx1 = n // 3
            idx2 = 2 * n // 3

            s1 = seq[:idx1]
            s2 = seq[idx1:idx2]
            s3 = seq[idx2:]

            # Ensure at least one element in each state
            if not s1:
                s1 = [seq[0]]
                s2 = seq[1:idx2]
            if not s2:
                s2 = [seq[idx1]]
                s3 = seq[idx1+1:]
            if not s3:
                s3 = [seq[-1]]
                s2 = seq[idx1:-1]

            # Adjust boundary between S1 and S2
            # Check left element first
            while len(s1) > 1:
                left_elem = s1[-1]
                dist_s1 = num_std_away(left_elem, params[0][0], params[0][1])
                dist_s2 = num_std_away(left_elem, params[1][0], params[1][1])

                if dist_s2 < dist_s1:
                    # Move to S2
                    s2 = [left_elem] + s2
                    s1 = s1[:-1]
                else:
                    break

            # Check right element
            while len(s2) > 1:
                right_elem = s2[0]
                dist_s1 = num_std_away(right_elem, params[0][0], params[0][1])
                dist_s2 = num_std_away(right_elem, params[1][0], params[1][1])

                if dist_s1 < dist_s2:
                    # Move to S1
                    s1 = s1 + [right_elem]
                    s2 = s2[1:]
                else:
                    break

            # Adjust boundary between S2 and S3
            # Check left element first
            while len(s2) > 1:
                left_elem = s2[-1]
                dist_s2 = num_std_away(left_elem, params[1][0], params[1][1])
                dist_s3 = num_std_away(left_elem, params[2][0], params[2][1])

                if dist_s3 < dist_s2:
                    # Move to S3
                    s3 = [left_elem] + s3
                    s2 = s2[:-1]
                else:
                    break

            # Check right element
            while len(s3) > 1:
                right_elem = s3[0]
                dist_s2 = num_std_away(right_elem, params[1][0], params[1][1])
                dist_s3 = num_std_away(right_elem, params[2][0], params[2][1])

                if dist_s2 < dist_s3:
                    # Move to S2
                    s2 = s2 + [right_elem]
                    s3 = s3[1:]
                else:
                    break

            new_states[0].extend(s1)
            new_states[1].extend(s2)
            new_states[2].extend(s3)

        # Update parameters
        old_params = params
        params = [calculate_mean_std(new_states[i]) for i in range(3)]

        print(f"\nIteration {iteration + 1}:")
        for i in range(3):
            print(f"  State {i+1}: mean={params[i][0]}, std={params[i][1]}, count={len(new_states[i])}")

        # Check for convergence
        if params == old_params:
            print(f"✓ Converged after {iteration + 1} iterations")
            states = new_states
            break
        states = new_states
    else:
        print(f"⚠ Did not converge after {max_iterations} iterations")

    # Calculate transition probabilities
    print(f"\n{'='*70}")
    print(f"Final Results for {word_name}:")
    print(f"{'='*70}")

    # Emission parameters
    print(f"\nEmission parameters:")
    for i in range(3):
        print(f"  State {i+1}: mean={params[i][0]}, std={params[i][1]}")

    # Transition probabilities
    # Count observations per state and number of sequences
    num_sequences = len(data_list)
    counts = [len(states[i]) for i in range(3)]

    # Each state transitions to the next state exactly num_sequences times
    # The rest are self-transitions
    print(f"\nTransition counts:")
    print(f"  State 1: total={counts[0]}, exits={num_sequences}, self={counts[0] - num_sequences}")
    print(f"  State 2: total={counts[1]}, exits={num_sequences}, self={counts[1] - num_sequences}")
    print(f"  State 3: total={counts[2]}, exits={num_sequences}, self={counts[2] - num_sequences}")

    # Calculate probabilities
    p_s1_s2 = round(num_sequences / counts[0], 3) if counts[0] > 0 else 0.0
    p_s1_s1 = round(1 - p_s1_s2, 3)

    p_s2_s3 = round(num_sequences / counts[1], 3) if counts[1] > 0 else 0.0
    p_s2_s2 = round(1 - p_s2_s3, 3)

    p_s3_end = round(num_sequences / counts[2], 3) if counts[2] > 0 else 0.0
    p_s3_s3 = round(1 - p_s3_end, 3)

    print(f"\nTransition probabilities:")
    print(f"  P(S1->S1) = {p_s1_s1}, P(S1->S2) = {p_s1_s2}")
    print(f"  P(S2->S2) = {p_s2_s2}, P(S2->S3) = {p_s2_s3}")
    print(f"  P(S3->S3) = {p_s3_s3}, P(S3->end) = {p_s3_end}")

    return params, (p_s1_s1, p_s1_s2, p_s2_s2, p_s2_s3, p_s3_s3, p_s3_end)

# Train all words
results = {}
for word in ['ALLIGATOR', 'NUTS', 'SLEEP']:
    results[word] = train_hmm(word, training_data[word])

# Print summary for easy copy-paste
print(f"\n\n{'='*70}")
print("SUMMARY - For part_1_a()")
print(f"{'='*70}")

for word, prefix in [('ALLIGATOR', 'A'), ('NUTS', 'N'), ('SLEEP', 'S')]:
    params, trans = results[word]
    print(f"\n{word}:")
    print(f"  prior_probs = {{'{prefix}1': 1.0, '{prefix}2': 0.0, '{prefix}3': 0.0, '{prefix}end': 0.0}}")
    print(f"  transition_probs = {{")
    print(f"    '{prefix}1': {{'{prefix}1': {trans[0]}, '{prefix}2': {trans[1]}, '{prefix}3': 0.0, '{prefix}end': 0.0}},")
    print(f"    '{prefix}2': {{'{prefix}1': 0.0, '{prefix}2': {trans[2]}, '{prefix}3': {trans[3]}, '{prefix}end': 0.0}},")
    print(f"    '{prefix}3': {{'{prefix}1': 0.0, '{prefix}2': 0.0, '{prefix}3': {trans[4]}, '{prefix}end': {trans[5]}}},")
    print(f"    '{prefix}end': {{'{prefix}1': 0.0, '{prefix}2': 0.0, '{prefix}3': 0.0, '{prefix}end': 1.0}}")
    print(f"  }}")
    print(f"  emission_paras = {{")
    print(f"    '{prefix}1': {params[0]},")
    print(f"    '{prefix}2': {params[1]},")
    print(f"    '{prefix}3': {params[2]},")
    print(f"    '{prefix}end': (None, None)")
    print(f"  }}")
