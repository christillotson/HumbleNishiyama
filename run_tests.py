# TESTING OUT METHOD ONE and its ability to generate the data into the data/method_1 folder

from src.method_2 import DecksStr

NUM_DECKS_TO_TEST = [1_000, 10_000, 100_000, 1_000_000, 2_000_000]

for num_decks in NUM_DECKS_TO_TEST:
    decks = DecksStr(num_decks=num_decks)
    print(decks.decks.shape)       # (10, 52)
    #print(decks_2million.decks.sum(axis=1)) # each row sums to 26
    print(decks.decks.nbytes, "bytes")
    print(decks.decks.nbytes / (1024**2), "MB")
    print('---')