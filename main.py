from src.benchmarks import benchmark_dp_vs_naive
from src.experiment import run_real_experiment

if __name__ == "__main__":
    benchmark_dp_vs_naive(n=50000, window=30, reps=500)
    run_real_experiment(window=5, threshold=0.0)
