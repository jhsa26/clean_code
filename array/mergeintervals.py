def merge(intervals):
    out = []
    for i in sorted(intervals, key = lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out.append(i)
    return out
