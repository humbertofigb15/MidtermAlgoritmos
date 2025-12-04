from dataclasses import dataclass
from datetime import date
from typing import List, Tuple

@dataclass
class TimeSeriesPoint:
    date: date
    value: float

def convert_to_timeseries(data: List[Tuple[date, float]]) -> List[TimeSeriesPoint]:
    return [TimeSeriesPoint(d, v) for d, v in data]

def compute_daily_returns(ts: List[TimeSeriesPoint]) -> List[float]:
    returns = []
    for i in range(len(ts) - 1):
        delta = ts[i + 1].value - ts[i].value
        returns.append(delta)
    return returns
