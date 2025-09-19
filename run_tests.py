import os
import numpy as np
from src.run_methods_as_functions import method_1_funct, method_2_funct
from src.results import summarize_experiments_to_file
from src.write_markdown import write_DataGeneration

# Path to where statistics about each run are stored.
wrapper_log_path = "./data/wrapper_log.txt"
# Path to where meta-statistics (mean, std, etc) about each unique parameter combination are stored.
summary_log_path = "./data/experiment_summary.txt"

# Deleting wrapper_log.txt and experiment_summary.txt files if they already exist, 
# so that any tests run in the program are the only ones recorded.

if os.path.exists(wrapper_log_path):
    os.remove(wrapper_log_path)
    print("We found an existing test log file with data already in it -- it has been deleted.")

if os.path.exists(summary_log_path):
    os.remove(summary_log_path)
    print("We found an existing statistical summary log file with data already in it -- it has been deleted.")

# We will run 5 experiments, on 5 different numbers of decks of cards.
# For now this should be same length as num times to run experiment.
NUM_DECKS_TO_TEST = [1_000, 10_000, 100_000, 1_000_000, 2_000_000] 

# For each number of cards we will get the mean, median, and stdev of runtime, storage, and memory, 
# for a certain number of repetitions (this constant).
# There will be more repititions for smaller values of num_decks, and fewer repitions for larger values of num_decks, 
# so that we can save on runtime for now.
# Minimum value should be 5 (up to programmer though) for size of a "small sample"
# For now this should be same length as num decks to test.
# Each number corresponds, in the same index, to the number of decks to test.
NUM_TIMES_TO_RUN_EXPERIMENT = [30, 20, 10, 5, 5]

# We are going to start at random seed 440, and add 1 to that seed with each iteration.
# This should probably be implemented differently later to ensure true randomness.
random_seed = 440

# Go through each num decks
for i, num_decks in enumerate(NUM_DECKS_TO_TEST):
    print(f'Generating {num_decks} decks {NUM_TIMES_TO_RUN_EXPERIMENT[i]*2} times ({NUM_TIMES_TO_RUN_EXPERIMENT[i]} times for each of 2 methods)...')

    # Get the number of times to run experiment from the corresponding index i of NUM_DECKS_TO_TEST
    for rep in range(NUM_TIMES_TO_RUN_EXPERIMENT[i]):
        random_seed += 1

        # Run the unique number of decks on each method
        decks_method_1 = method_1_funct(num_decks=num_decks, random_seed=random_seed)
        decks_method_2 = method_2_funct(num_decks=num_decks, random_seed=random_seed) 

# Write to the experiment_summary.txt from wrapper_log.txt
summarize_experiments_to_file(wrapper_log_path)

# Get explanatory paragraphs and combine with experiment_summary.txt into DataGeneration.md
write_DataGeneration()

#    FUTURE:
        # This should probably be refactored to draw from a config.py with paths defined there.
        # The Num decks to test and num times for each should be implemented more elegantly
