from .dp_engine import DPWindowEngine
from typing import List

def dp_greedy_predict(returns: List[float], window: int, threshold: float = 0.0):
    dp = DPWindowEngine(returns)
    preds = []

    for p in range(window - 1, len(returns)):
        start_idx = p - (window - 1)
        s = dp.range_sum(start_idx, window)
        preds.append(1 if s > threshold else -1)

    return preds

def moving_average_predict(values: List[float], window: int):
    preds = []
    for t in range(window, len(values)):
        prev_window = values[t - window:t]
        avg = sum(prev_window) / window
        preds.append(1 if values[t] > avg else -1)
    return preds
