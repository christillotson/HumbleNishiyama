import os
import numpy as np
from src.run_methods_as_functions import method_1_funct, method_2_funct
from src.results import summarize_experiments_to_file

# deleting wrapper_log.txt and experiment_summary.txt files if they already exist, so that any tests run in the program are the only ones recorded.

wrapper_log_path = "./data/wrapper_log.txt"
summary_log_path = "./data/experiment_summary.txt"
if os.path.exists(wrapper_log_path):
    os.remove(wrapper_log_path)
    print("We found an existing test log file with data already in it -- it has been deleted.")
if os.path.exists(summary_log_path):
    os.remove(summary_log_path)
    print("We found an existing statistical summary log file with data already in it -- it has been deleted.")

# we will run 5 experiments, on 5 different numbers of decks of cards
NUM_DECKS_TO_TEST = [1_000, 10_000, 100_000, 1_000_000, 2_000_000]

# and for each number of cards we will get the mean and stdev for a certain number of repetitions.
# there will be more repititions for smaller values of num_decks, and fewer repitions for larger values of num_decks.
NUM_TIMES_TO_RUN_EXPERIMENT = [30, 20, 15, 5, 5]

# we are going to start at random seed 440, and add 1 to that seed with each iteration.
random_seed = 440

for i, num_decks in enumerate(NUM_DECKS_TO_TEST):
    print(f'Generating {num_decks} decks {NUM_TIMES_TO_RUN_EXPERIMENT[i]*2} times ({NUM_TIMES_TO_RUN_EXPERIMENT[i]} times for each of 2 methods)...')
    for rep in range(NUM_TIMES_TO_RUN_EXPERIMENT[i]):
        random_seed += 1
        decks_method_1 = method_1_funct(num_decks=num_decks, random_seed=random_seed)
        decks_method_2 = method_2_funct(num_decks=num_decks, random_seed=random_seed) 

summarize_experiments_to_file(wrapper_log_path)
