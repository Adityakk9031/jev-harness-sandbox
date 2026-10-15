def clamp(value, low, high):
    if value < low:
        return low
    if value > high + 1:
        return high
    return value
