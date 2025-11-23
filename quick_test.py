import sys
sys.path.insert(0, 'submission')

try:
    from submission import part_1_a, viterbi, part_2_a, multidimensional_viterbi, return_your_name, gaussian_prob
    print("[PASS] All functions imported successfully")
    
    # Test part_1_a
    result = part_1_a()
    print(f"[PASS] part_1_a returns {len(result)} items")
    
    a_prior, a_trans, a_emis, n_prior, n_trans, n_emis, s_prior, s_trans, s_emis = result
    
    # Check transition probabilities
    print(f"\n[CHECK] ALLIGATOR transition probs:")
    print(f"  A1->A1: {a_trans['A1']['A1']}, A1->A2: {a_trans['A1']['A2']}")
    print(f"  A2->A2: {a_trans['A2']['A2']}, A2->A3: {a_trans['A2']['A3']}")
    print(f"  A3->A3: {a_trans['A3']['A3']}, A3->Aend: {a_trans['A3']['Aend']}")
    
    print(f"\n[CHECK] NUTS transition probs:")
    print(f"  N1->N1: {n_trans['N1']['N1']}, N1->N2: {n_trans['N1']['N2']}")
    print(f"  N2->N2: {n_trans['N2']['N2']}, N2->N3: {n_trans['N2']['N3']}")
    print(f"  N3->N3: {n_trans['N3']['N3']}, N3->Nend: {n_trans['N3']['Nend']}")
    
    print(f"\n[CHECK] SLEEP transition probs:")
    print(f"  S1->S1: {s_trans['S1']['S1']}, S1->S2: {s_trans['S1']['S2']}")
    print(f"  S2->S2: {s_trans['S2']['S2']}, S2->S3: {s_trans['S2']['S3']}")
    print(f"  S3->S3: {s_trans['S3']['S3']}, S3->Send: {s_trans['S3']['Send']}")
    
    # Check prior probabilities
    print(f"\n[CHECK] Prior probabilities:")
    a_sum = sum(a_prior.values())
    n_sum = sum(n_prior.values())
    s_sum = sum(s_prior.values())
    total = a_sum + n_sum + s_sum
    print(f"  ALLIGATOR: {a_sum}, NUTS: {n_sum}, SLEEP: {s_sum}")
    print(f"  Total: {total}")
    if abs(total - 1.0) < 0.01:
        print(f"[PASS] Prior probabilities sum correctly")
    else:
        print(f"[FAIL] Prior probabilities sum to {total}, expected 1.0")
    
    # Test return_your_name
    name = return_your_name()
    print(f"\n[CHECK] return_your_name() returns: '{name}'")
    
    print("\n[SUCCESS] All basic checks passed!")
    
except Exception as e:
    print(f"[FAIL] Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
