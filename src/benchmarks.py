import time, random
from .dp_engine import DPWindowEngine, naive_window_sum

def benchmark_dp_vs_naive(n=50000, window=30, reps=500):
    values = [random.uniform(-0.05, 0.05) for _ in range(n)]
    dp = DPWindowEngine(values)
    starts = [random.randint(0, n - window) for _ in range(reps)]

    t0 = time.perf_counter()
    for s in starts:
        naive_window_sum(values, s, window)
    naive_time = time.perf_counter() - t0

    t0 = time.perf_counter()
    for s in starts:
        dp.range_sum(s, window)
    dp_time = time.perf_counter() - t0

    print("\nBenchmark: DP vs Naive")
    print(f"Naive : {naive_time:.6f}s")
    print(f"DP    : {dp_time:.6f}s")
    print(f"Speedup = {naive_time / dp_time:.2f}x")
