# code that runs methods 1 and 2 for the metrics:
# run + write times, storage space, memory usage, and read times

from src.method_1 import DecksInt
from src.method_2 import DecksStr
from src.timer import timer

@timer
def method_1_funct(num_decks, random_seed, write_decks_to_file = True, base_path = "../data/method_1/"):
    """
    a function that runs the class DecksInt (method_1).
    The reason for this is so that the wrapper (which works on functions) that runs quantitative tests on our output
    can actually run effectively. 
    """
    decks = DecksInt(num_decks, random_seed, write_decks_to_file = True, base_path = "../data/method_1/")
    return decks.decks

@timer
def method_2_funct(num_decks, random_seed, write_decks_to_file = True, base_path = "../data/method_2/"):
    """    
    a function that runs the class DecksStr (method_2).
    The reason for this is so that the wrapper (which works on functions) that runs quantitative tests on our output
    can actually run effectively.    
    """
    decks = DecksStr(num_decks, random_seed, write_decks_to_file = True, base_path = "../data/method_2/")
    return decks.decks