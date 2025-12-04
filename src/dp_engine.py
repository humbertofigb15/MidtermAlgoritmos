class DPWindowEngine:
    def __init__(self, values):
        self.values = values
        self.prefix = self._build_prefix(values)

    @staticmethod
    def _build_prefix(values):
        prefix = [0.0] * (len(values) + 1)
        acc = 0.0
        for i, v in enumerate(values):
            acc += v
            prefix[i + 1] = acc
        return prefix

    def range_sum(self, start_index, window):
        end = start_index + window
        return self.prefix[end] - self.prefix[start_index]

def naive_window_sum(values, start_index, window):
    total = 0.0
    for i in range(start_index, start_index + window):
        total += values[i]
    return total
