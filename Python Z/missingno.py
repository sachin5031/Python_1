# Missing Number Finder
def find_missing_number(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    full_set = set(range(min_num, max_num + 1))
    actual_set = set(numbers)
    missing = full_set - actual_set

    if len(missing) == 1:
        return missing.pop()
    elif len(missing) == 0:
        return "No number is missing."
    else:
        return f"Multiple numbers missing: {sorted(missing)}"
