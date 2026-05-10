def detect_shift(original, modified):
    original_words = set(original.lower().split())
    modified_words = set(modified.lower().split())

    removed = original_words - modified_words
    added = modified_words - original_words

    return {
        "removed": list(removed),
        "added": list(added),
        "possible_drift": len(removed) + len(added) > 5
    }
