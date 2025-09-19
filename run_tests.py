import os
import numpy as np
from src.run_methods_as_functions import method_1_funct, method_2_funct

# deleting wrapper_log.txt if it already exists, so that any tests run in the program are the only ones recorded.

wrapper_log_path = "./data/wrapper_log.txt"
if os.path.exists(wrapper_log_path):
    os.remove(wrapper_log_path)
    print("We found an existing test log file with data already in it -- it has been deleted.")

# we will run 5 experiments, on 5 different numbers of decks of cards
NUM_DECKS_TO_TEST = [1_000, 10_000, 100_000]

# and for each number of cards we will get the mean and stdev for a certain number of repetitions.
# there will be more repititions for smaller values of num_decks, and fewer repitions for larger values of num_decks.
NUM_TIMES_TO_RUN_EXPERIMENT = [30, 15, 10]

# we are going to start at random seed 440, and add 1 to that seed with each iteration.
random_seed = 440

for i, num_decks in enumerate(NUM_DECKS_TO_TEST):
    print(f'Generating {num_decks} decks {NUM_TIMES_TO_RUN_EXPERIMENT[i]} times...')
    for rep in range(NUM_TIMES_TO_RUN_EXPERIMENT[i]):
        random_seed += 1
        decks_method_1 = method_1_funct(num_decks=num_decks, random_seed=random_seed)
        decks_method_2 = method_2_funct(num_decks=num_decks, random_seed=random_seed) 