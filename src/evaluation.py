from dataclasses import dataclass
from typing import List

@dataclass
class EvaluationResult:
    accuracy: float
    n_samples: int
    n_up_pred: int
    n_down_pred: int
    n_up_true: int
    n_down_true: int

def sign_from_returns(returns: List[float]) -> List[int]:
    return [1 if r > 0 else -1 for r in returns]

def align_truth_for_dp(returns: List[float], window: int) -> List[int]:
    signs = sign_from_returns(returns)
    return [signs[i + 1] for i in range(window - 1, len(returns) - 1)]

def align_truth_for_ma(returns: List[float], window: int):
    signs = sign_from_returns(returns)
    return signs[window:]

def evaluate_predictions(preds, truth):
    correct = sum(1 for p, t in zip(preds, truth) if p == t)
    accuracy = correct / len(truth)

    return EvaluationResult(
        accuracy=accuracy,
        n_samples=len(truth),
        n_up_pred=sum(1 for p in preds if p == 1),
        n_down_pred=sum(1 for p in preds if p == -1),
        n_up_true=sum(1 for t in truth if t == 1),
        n_down_true=sum(1 for t in truth if t == -1),
    )
