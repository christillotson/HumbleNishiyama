import os
import numpy as np
import pandas as pd
import random
from src.run_methods_as_functions import method_1_funct, method_2_funct
from src.results import summarize_experiments_to_file
from src.write_markdown import write_DataGeneration
from src.scoring import import_decks, batch_score_all_combos
from src.db_code.interact_db import create_empty, add_new, read_db

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

try:
    num_decks_to_generate = int(input("Please enter, with no commas or spaces, the number of new decks you want to generate and score: "))
except:
    print("Something's gone wrong with how you entered the number. Please try again later.")
random_seed = random.randint(1, 1_000_000)
print(f'To confirm, you are generating {num_decks_to_generate} decks with a randomly selected seed of {random_seed}.')
print('Generating now!....')
#NUM_DECKS_TO_TEST = [1_000, 10_000, 100_000, 1_000_000, 2_000_000] 

# For each number of cards we will get the mean, median, and stdev of runtime, storage, and memory, 
# for a certain number of repetitions (this constant).
# There will be more repititions for smaller values of num_decks, and fewer repitions for larger values of num_decks, 
# so that we can save on runtime for now.
# Minimum value should be 5 (up to programmer though) for size of a "small sample"
# For now this should be same length as num decks to test.
# Each number corresponds, in the same index, to the number of decks to test.
#NUM_TIMES_TO_RUN_EXPERIMENT = [30, 20, 10, 5, 5]

# We are going to start at random seed 440, and add 1 to that seed with each iteration.
# This should probably be implemented differently later to ensure true randomness.
#random_seed = 440

# # Go through each num decks
# for i, num_decks in enumerate(NUM_DECKS_TO_TEST):
#     print(f'Generating {num_decks} decks {NUM_TIMES_TO_RUN_EXPERIMENT[i]*2} times ({NUM_TIMES_TO_RUN_EXPERIMENT[i]} times for each of 2 methods)...')

#     # Get the number of times to run experiment from the corresponding index i of NUM_DECKS_TO_TEST
#     for rep in range(NUM_TIMES_TO_RUN_EXPERIMENT[i]):
#         random_seed += 1

#         # Run the unique number of decks on each method
#         decks_method_1 = method_1_funct(num_decks=num_decks, random_seed=random_seed)
#         decks_method_2 = method_2_funct(num_decks=num_decks, random_seed=random_seed) 

decks_method_1 = method_1_funct(num_decks = num_decks_to_generate, random_seed = random_seed)

# Write to the experiment_summary.txt from wrapper_log.txt
summarize_experiments_to_file(wrapper_log_path)

# --------------------------------------

PATH_TO_DB_SNAPSHOT = "./data/db_out/database_output.csv"

# Hardcoded deck to test our functionality. Only 1000 decks. Commented code below will iterate over all decks (takes forever)
subfolder_name = f'{num_decks_to_generate}_decks_seed_{random_seed}'
decks_to_score = import_decks(subfolder_name = subfolder_name)
decks_to_score_df= batch_score_all_combos(decks_to_score)

print(decks_to_score_df)

# create_empty() 
# # uncommenting and running immediately above will reset the database

# Add this data to the database
add_new(decks_to_score_df)

database_now = read_db() # REFERENCE THIS DF DURING HEATMAP GENERATION!!!

print(database_now) # optional print to see database output

def save_df_to_csv(df: pd.DataFrame, path: str):

    # Separate the directory from the file path
    directory = os.path.dirname(path)

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

    # If the file exists, remove it
    if os.path.exists(path):
        print(f"Removing old database snapshot: {path}")
        os.remove(path)

    # Save DataFrame to CSV
    df.to_csv(path, index=False)
    print(f"Saving database contents as: {path}")

save_df_to_csv(database_now, PATH_TO_DB_SNAPSHOT)