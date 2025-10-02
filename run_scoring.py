# run this script in order to perform scoring on a selected subset of our data
# we have chosen to do this on one of our generated files of 1000 decks of cards :) feel free to change this

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

print(read_db())

## todo: save the output of read_db as a csv

