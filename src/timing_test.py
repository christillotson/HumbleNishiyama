import time
from timer import timer

@timer
def test_func(num_decks = 1000, random_seed = 440, write_decks_to_file = True, base_path = "../data/method_1/"):

    print('ran test_func')
    time.sleep(5)

    return 200

test_func(1000)