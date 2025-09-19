import pandas as pd
import os

def summarize_experiments_to_file(log_path: str, filename: str = "experiment_summary.txt") -> None:
    """
    For each experiment (unique num_decks), prints stats for each method consecutively,
    compute mean, median, and std of numeric columns,
    save results to a text file, and print to console.
    """

    df = pd.read_csv(log_path)

    # Ensure the data folder exists
    data_folder = "./data"
    os.makedirs(data_folder, exist_ok=True)
    filepath = os.path.join(data_folder, filename)

    # Compute stats only for numeric columns
    numeric_cols = ["storage_bytes", "memory_bytes", "time_taken"]
    
    # Group by num_decks first, then method
    grouped = df.groupby(["num_decks", "method"])
    summary = grouped[numeric_cols].agg(["mean", "median", "std"])

    print("-------------------")
    print("RESULTS:")
    print("-------------------")
    # Open file for writing
    with open(filepath, "w", encoding="utf-8") as f:
        # Loop over num_decks first
        for num_decks in sorted(df["num_decks"].unique()):
            # Get all methods for this experiment
            methods = df[df["num_decks"] == num_decks]["method"].unique()
            for method in methods:
                header = f"\n=== Method: {method} | num_decks: {num_decks} ==="
                print(header)
                f.write(header + "\n")
                
                for col in numeric_cols:
                    mean_val = summary.loc[(num_decks, method), (col, "mean")]
                    median_val = summary.loc[(num_decks, method), (col, "median")]
                    std_val = summary.loc[(num_decks, method), (col, "std")]
                    line = f"{col:15s} | mean={mean_val:10.2f} | median={median_val:10.2f} | std={std_val:10.2f}"
                    print(line)
                    f.write(line + "\n")

    print(f"\nSummary saved to {filepath}")
