import os
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from src.run_methods_as_functions import method_1_funct, method_2_funct
from src.results import summarize_experiments_to_file
from src.write_markdown import write_DataGeneration
from src.scoring import import_decks, batch_score_all_combos
from src.db_code.interact_db import create_empty, add_new, read_db
from src.heatmap import make_heatmap

# Path to where statistics about each run are stored.
wrapper_log_path = "./data/wrapper_log.txt"
# Path to where meta-statistics (mean, std, etc) about each unique parameter combination are stored.
summary_log_path = "./data/experiment_summary.txt"

PATH_TO_DB = os.path.join('src','db_code','database','HN_DB')
PATH_TO_EMPTY = os.path.join('src','db_code','empty_hn_data.csv')

PATH_TO_DB_SNAPSHOT = "./data/db_out/database_output.csv"


# Deleting wrapper_log.txt and experiment_summary.txt files if they already exist, 
# so that any tests run in the program are the only ones recorded.

if not os.path.exists(PATH_TO_DB):
    create_empty(path_string = PATH_TO_DB, path_to_empty = PATH_TO_EMPTY)

if os.path.exists(wrapper_log_path):
    os.remove(wrapper_log_path)
    #print("We found an existing test log file with data already in it -- it has been deleted.")

if os.path.exists(summary_log_path):
    os.remove(summary_log_path)
    #print("We found an existing statistical summary log file with data already in it -- it has been deleted.")

try:
    num_decks_to_generate = int(input("Please enter, with no commas or spaces, \nthe number of new decks you want to generate and score, or 0 to just get heatmaps: "))
except:
    print("Something's gone wrong with how you entered the number. Please try again later.")

if num_decks_to_generate != 0:
    random_seed = random.randint(1, 1_000_000)
    print(f'To confirm, you are generating {num_decks_to_generate} decks with a randomly selected seed of {random_seed}.')
    print('Generating now!....')
    decks_method_1 = method_1_funct(num_decks = num_decks_to_generate, random_seed = random_seed)

    # Write to the experiment_summary.txt from wrapper_log.txt
    summarize_experiments_to_file(wrapper_log_path)

    # --------------------------------------

    subfolder_name = f'{num_decks_to_generate}_decks_seed_{random_seed}'
    decks_to_score = import_decks(subfolder_name = subfolder_name)
    decks_to_score_df= batch_score_all_combos(decks_to_score)

    print(decks_to_score_df)

    # create_empty() 
    # # uncommenting and running immediately above will reset the database

    # Add this data to the database
    add_new(data_DF = decks_to_score_df, path_string = PATH_TO_DB)

database_now = read_db(path_string = PATH_TO_DB) # REFERENCE THIS DF DURING HEATMAP GENERATION!!!

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

print('------------------------------------')

# PATH_TO_DB = os.path.join('src', 'db_code', 'database', 'HN_DB')
# card_df = read_db(PATH_TO_DB)

make_heatmap(scoring_method = "tricks", input_df = database_now)

make_heatmap(scoring_method = "cards", input_df = database_now)