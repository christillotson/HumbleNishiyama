import os

def write_DataGeneration():
    # 1. Check if DataGeneration.md exists in the current directory, and delete if it does
    output_file = "DataGeneration.md"
    if os.path.exists(output_file):
        print("DataGeneration.md exists. Removing it to add new version.")
        os.remove(output_file)

    # 2a. Read text from Explanation.txt
    with open("Explanation.txt", "r", encoding="utf-8") as f:
        explanation_text = f.read()

    # 3a. Read text from /data/experiment_summary.txt
    with open(os.path.join("data", "experiment_summary.txt"), "r", encoding="utf-8") as f:
        experiment_summary_text = f.read()

    # 2. Create DataGeneration.md and write contents
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(explanation_text)
        f.write("\n")  # ensure newline after Explanation.txt content
        f.write(experiment_summary_text)
