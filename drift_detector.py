def detect_meaning_shift(original, modified):
    """
    Very simple comparison to flag potential meaning drift.
    This is not production-grade, but demonstrates the concept.
    """

    original_words = set(original.lower().split())
    modified_words = set(modified.lower().split())

    removed = original_words - modified_words
    added = modified_words - original_words

    return {
        "removed_terms": list(removed),
        "added_terms": list(added),
        "risk_flag": len(removed) > 3 or len(added) > 3
    }


if __name__ == "__main__":
    original = "The policy must be strictly enforced under all conditions."
    modified = "The policy should be followed in most situations."

    result = detect_meaning_shift(original, modified)
    print(result)
