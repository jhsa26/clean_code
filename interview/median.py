def median(vec):
    if not vec:
        return None
    if len(vec) % 2 == 0:
        return float(vec[len(vec)/2 - 1] + vec[len(vec)/2]) / 2
    return vec[len(vec)/2]

print median([2, 4, 5])
print median([2, 4, 6, 7])
