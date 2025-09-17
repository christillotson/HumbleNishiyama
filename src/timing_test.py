import time
from timer import timer

@timer
def test_func(num_decks, random_seed = 460, write_decks_to_file = True, base_path = "../data/method_1/"):

    print('ran test_func')
    time.sleep(5)

    return 200

test_func(20)
test_func(40)
test_func(60)