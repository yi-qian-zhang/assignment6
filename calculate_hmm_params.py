import numpy as np

# Training data for each word
training_data = {
    'ALLIGATOR': [
        ([31, 28, 28, 37, 68, 49, 64, 66, 22, 17, 53, 73, 81, 78, 48, 49, 47],
         [[31, 28, 28, 37, 68, 49], [64, 66, 22, 17, 53, 73], [81, 78, 48, 49, 47]]),
        ([25, 62, 75, 80, 75, 36, 74, 33, 27, 34],
         [[25, 62, 75, 80], [75, 36, 74, 33], [27, 34]]),
        ([-4, 69, 59, 45, 62, 22, 17, 28, 12, 14, 24, 32, 39, 61, 35, 32],
         [[-4, 69, 59, 45, 62, 22], [17, 28, 12, 14, 24, 32], [39, 61, 35, 32]])
    ],
    'NUTS': [
        ([45, 68, 62, 75, 61, 44, 73, 72, 71, 75, 55],
         [[45, 68, 62, 75], [61, 44, 73, 72], [71, 75, 55]]),
        ([33, 33, 32, 32, 34, 38, 43, 41, 35, 36, 36, 37, 38, 38, 39, 40, 38, 38],
         [[33, 33, 32, 32, 34, 38], [43, 41, 35, 36, 36, 37], [38, 38, 39, 40, 38, 38]]),
        ([33, 31, 29, 28, 25, 24, 25, 28, 28, 38, 37, 40, 37, 36, 36, 38, 44, 48, 48],
         [[33, 31, 29, 28, 25, 24, 25], [28, 28, 38, 37, 40, 37, 36], [36, 38, 44, 48, 48]])
    ],
    'SLEEP': [
        ([37, 35, 41, 39, 41, 38, 38, 38],
         [[37, 35, 41], [39, 41, 38], [38, 38]]),
        ([22, 17, 18, 35, 33, 36, 42, 36, 41, 41, 37, 38],
         [[22, 17, 18, 35], [33, 36, 42, 36], [41, 41, 37, 38]]),
        ([38, 37, 35, 32, 35, 13, 36, 41, 41, 31, 32, 34, 34],
         [[38, 37, 35, 32, 35], [13, 36, 41, 41, 31], [32, 34, 34]])
    ]
}

def calculate_mean_std(values):
    """Calculate mean and standard deviation, rounded to 3 decimals"""
    mean = np.mean(values)
    std = np.std(values, ddof=0)  # Population std
    return round(mean, 3), round(std, 3)

def closer_to_state(observation, state1_params, state2_params):
    """Check which state an observation is closer to in terms of standard deviations"""
    mean1, std1 = state1_params
    mean2, std2 = state2_params

    dist1 = abs(observation - mean1) / std1
    dist2 = abs(observation - mean2) / std2

    return 1 if dist1 < dist2 else 2

def train_hmm(word_name, sequences):
    """Train HMM using the method from Udacity Lesson 8-29"""
    print(f"\n{'='*60}")
    print(f"Training HMM for {word_name}")
    print(f"{'='*60}")

    # Initialize with given state assignments
    all_states = [[], [], []]
    for seq, initial_states in sequences:
        for i, state_vals in enumerate(initial_states):
            all_states[i].extend(state_vals)

    # Calculate initial means and stds
    state_params = []
    for i in range(3):
        mean, std = calculate_mean_std(all_states[i])
        state_params.append((mean, std))
        print(f"Initial State {i+1}: mean={mean}, std={std}")

    # Iteratively refine state boundaries
    max_iterations = 10
    for iteration in range(max_iterations):
        print(f"\nIteration {iteration + 1}:")
        new_states = [[], [], []]

        for seq, initial_states in sequences:
            # Start with initial division
            state_assignments = list(initial_states)

            # Adjust boundaries between states
            # Between state 1 and 2
            while len(state_assignments[0]) > 1:
                boundary_val = state_assignments[0][-1]
                which = closer_to_state(boundary_val, state_params[0], state_params[1])
                if which == 2:
                    # Move to state 2
                    state_assignments[1] = [boundary_val] + state_assignments[1]
                    state_assignments[0] = state_assignments[0][:-1]
                else:
                    break

            # Check from right side too
            while len(state_assignments[1]) > 1:
                boundary_val = state_assignments[1][0]
                which = closer_to_state(boundary_val, state_params[0], state_params[1])
                if which == 1:
                    # Move to state 1
                    state_assignments[0] = state_assignments[0] + [boundary_val]
                    state_assignments[1] = state_assignments[1][1:]
                else:
                    break

            # Between state 2 and 3
            while len(state_assignments[1]) > 1:
                boundary_val = state_assignments[1][-1]
                which = closer_to_state(boundary_val, state_params[1], state_params[2])
                if which == 2:
                    # Move to state 3
                    state_assignments[2] = [boundary_val] + state_assignments[2]
                    state_assignments[1] = state_assignments[1][:-1]
                else:
                    break

            # Check from right side too
            while len(state_assignments[2]) > 1:
                boundary_val = state_assignments[2][0]
                which = closer_to_state(boundary_val, state_params[1], state_params[2])
                if which == 1:
                    # Move to state 2
                    state_assignments[1] = state_assignments[1] + [boundary_val]
                    state_assignments[2] = state_assignments[2][1:]
                else:
                    break

            # Add to new states
            for i in range(3):
                new_states[i].extend(state_assignments[i])

        # Calculate new parameters
        old_params = state_params[:]
        state_params = []
        for i in range(3):
            mean, std = calculate_mean_std(new_states[i])
            state_params.append((mean, std))
            print(f"  State {i+1}: mean={mean}, std={std}, count={len(new_states[i])}")

        # Check convergence
        if old_params == state_params:
            print(f"Converged after {iteration + 1} iterations")
            break

        all_states = new_states

    # Calculate transition probabilities
    print(f"\nFinal State Parameters:")
    for i in range(3):
        print(f"  State {i+1}: mean={state_params[i][0]}, std={state_params[i][1]}")

    # Count transitions
    transition_counts = {f'S{i}': {f'S{j}': 0 for j in range(1, 5)} for i in range(1, 5)}

    for seq, _ in sequences:
        # Assign each observation to a state based on final parameters
        state_sequence = []
        current_state = 1

        # Reconstruct state sequence from final all_states
        # This is a simplified approach - in reality we'd track which observations belong to which states

    # For now, let's calculate transitions from the state assignments
    # Count self-transitions vs exits for each state
    s1_count = sum(len(state_assignments[0]) for _, initial_states in sequences for state_assignments in [initial_states])
    s2_count = sum(len(state_assignments[1]) for _, initial_states in sequences for state_assignments in [initial_states])
    s3_count = sum(len(state_assignments[2]) for _, initial_states in sequences for state_assignments in [initial_states])

    # Number of sequences
    num_sequences = len(sequences)

    # State 1: exits to state 2 exactly num_sequences times
    s1_exits = num_sequences
    s1_self = s1_count - s1_exits

    # State 2: exits to state 3 exactly num_sequences times
    s2_exits = num_sequences
    s2_self = s2_count - s2_exits

    # State 3: exits to end state exactly num_sequences times
    s3_exits = num_sequences
    s3_self = s3_count - s3_exits

    print(f"\nTransition Statistics:")
    print(f"  State 1: self={s1_self}, exit={s1_exits}, total={s1_count}")
    print(f"  State 2: self={s2_self}, exit={s2_exits}, total={s2_count}")
    print(f"  State 3: self={s3_self}, exit={s3_exits}, total={s3_count}")

    # Calculate probabilities
    p_s1_s1 = round(1 - s1_exits / s1_count, 3) if s1_count > 0 else 0
    p_s1_s2 = round(s1_exits / s1_count, 3) if s1_count > 0 else 0

    p_s2_s2 = round(1 - s2_exits / s2_count, 3) if s2_count > 0 else 0
    p_s2_s3 = round(s2_exits / s2_count, 3) if s2_count > 0 else 0

    p_s3_s3 = round(1 - s3_exits / s3_count, 3) if s3_count > 0 else 0
    p_s3_end = round(s3_exits / s3_count, 3) if s3_count > 0 else 0

    print(f"\nTransition Probabilities:")
    print(f"  P(S1->S1) = {p_s1_s1}, P(S1->S2) = {p_s1_s2}")
    print(f"  P(S2->S2) = {p_s2_s2}, P(S2->S3) = {p_s2_s3}")
    print(f"  P(S3->S3) = {p_s3_s3}, P(S3->end) = {p_s3_end}")

    return state_params, (p_s1_s1, p_s1_s2, p_s2_s2, p_s2_s3, p_s3_s3, p_s3_end)

# Train all words
for word in ['ALLIGATOR', 'NUTS', 'SLEEP']:
    train_hmm(word, training_data[word])
