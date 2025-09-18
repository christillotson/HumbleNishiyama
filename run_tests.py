# TESTING OUT METHOD TWO and its ability to generate the data into the data/method_2 folder

from src.method_2 import DecksStr

NUM_DECKS_TO_TEST = [1_000, 10_000, 100_000, 1_000_000, 2_000_000]

for num_decks in NUM_DECKS_TO_TEST:
    decks = DecksStr(num_decks=num_decks)
    print(decks.decks.shape)       # (10, 52)
    #print(decks_2million.decks.sum(axis=1)) # each row sums to 26
    print(decks.decks.nbytes, "bytes")
    print(decks.decks.nbytes / (1024**2), "MB")
    print('---')

# This will create the data directory for method_2 if it does not exist, so it is safe to delete the data folder.