from datetime import date, timedelta

from .banxico_client import BanxicoClient
from .data_utils import convert_to_timeseries, compute_daily_returns
from .predictors import dp_greedy_predict, moving_average_predict
from .evaluation import (
    align_truth_for_dp, align_truth_for_ma, evaluate_predictions
)

def run_real_experiment(window=5, threshold=0.0):
    client = BanxicoClient()

    end = date.today()
    start = end - timedelta(days=730)
    raw = client.get_usd_mxn_range(start, end)

    ts = convert_to_timeseries(raw)
    prices = [p.value for p in ts]
    returns = compute_daily_returns(ts)

    dp_preds = dp_greedy_predict(returns, window, threshold)
    dp_truth = align_truth_for_dp(returns, window)
    L = min(len(dp_preds), len(dp_truth))
    dp_eval = evaluate_predictions(dp_preds[:L], dp_truth[:L])

    ma_preds = moving_average_predict(prices, window)
    ma_truth = align_truth_for_ma(returns, window)
    L2 = min(len(ma_preds), len(ma_truth))
    ma_eval = evaluate_predictions(ma_preds[:L2], ma_truth[:L2])

    print("\nReal Banxico Results")
    print(f"Window = {window}")
    print("\nDP+Greedy:", dp_eval)
    print("\nMA Baseline:", ma_eval)
    print(f"\nΔ Accuracy = {dp_eval.accuracy - ma_eval.accuracy:.3f}")
