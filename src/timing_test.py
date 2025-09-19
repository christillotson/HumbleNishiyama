import time
from timer import timer
import numpy as np

@timer
def test_func(base_path, num_decks, random_seed, write_decks_to_file = True):

    print('ran test_func')
    time.sleep(5)


    decks = np.array([10,2,2,124,34,1,213])

    return decks

test_func(base_path = "../data/method_1/", num_decks = 10000, random_seed = 440)
test_func(base_path = "../data/method_1/", num_decks = 100000, random_seed = 440)
test_func(base_path = "../data/method_1/", num_decks = 1000000, random_seed = 440, write_decks_to_file = False)