# run this script in order to perform scoring on a selected subset of our data
# we have chosen to do this on one of our generated files of 1000 decks of cards :) feel free to change this
import pandas as pd
import os

from src.scoring import import_decks, batch_score_all_combos
from src.create_empty_db import create_empty
from src.add_new_data_db import add_new
from src.read_db import read_db

decks_10k = import_decks(subfolder_name = '1000_decks_seed_441')
decks_10k_df= batch_score_all_combos(decks_10k)

print(decks_10k_df)

# create_empty() 
# # running above will reset the database

add_new(decks_10k_df)

database_now = read_db()

print(database_now) # optional print

## todo: save the output of read_db as a csv

def save_df_to_csv(df: pd.DataFrame, path: str):
    # If file exists, remove it
    if os.path.exists(path):
        print(f"removing old database snapshot {path}")
        os.remove(path)
    # Save DataFrame to CSV
    df.to_csv(path, index=False)
    print(f"Saving database contents as {path}")


save_df_to_csv(database_now, "./db_out/database_output.csv")

# ### Below is code to iterate over all decks

# def get_folder_names(path: str):
#     return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
# folders = get_folder_names("./data/method_1")
# print(folders)

# for subfolder in folders:

#     decks_object = import_decks(subfolder_name = subfolder)
#     score_df = batch_score_all_combos(decks_object)

#     # print(decks_10k_df)

#     # create_empty() 
#     # # running above will reset the database

#     add_new(score_df)

# database_now = read_db()

# print(database_now)

# save_df_to_csv(database_now, "database_output.csv")

### END MANY DECK CODE
