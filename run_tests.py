import numpy as np
from src.run_methods_as_functions import method_1, method_2

# we will run 5 experiments, on 5 different numbers of decks of cards
NUM_DECKS_TO_TEST = [1_000, 10_000, 100_000, 1_000_000, 2_000_000]

# and for each number of cards we will get the mean and stdev for a certain number of repetitions.
# there will be more repititions for smaller values of num_decks, and fewer repitions for larger values of num_decks.
NUM_TIMES_TO_RUN_EXPERIMENT = [30, 30, 20, 10, 10]

# we are going to start at random seed 440, and add 1 to that seed with each iteration.
random_seed = 440

for num_decks in NUM_DECKS_TO_TEST:
    for rep in NUM_TIMES_TO_RUN_EXPERIMENT:
        random_seed += 1
        decks_method_1 = method_1(num_decks=num_decks, random_seed=random_seed)
        decks_method_2 = method_2(num_decks=num_decks, random_seed=random_seed)

# for num_decks in NUM_DECKS_TO_TEST:
#     decks = DecksStr(num_decks=num_decks)
#     print(decks.decks.shape)       # (10, 52)
#     #print(decks_2million.decks.sum(axis=1)) # each row sums to 26
#     print(decks.decks.nbytes, "bytes")
#     print(decks.decks.nbytes / (1024**2), "MB")
#     print('---')