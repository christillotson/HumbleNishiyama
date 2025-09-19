from src.method_1 import DecksInt
from src.method_2 import DecksStr
from src.timer import timer

# Code that runs methods 1 and 2 for the metrics:
# Run times, storage space, memory usage
# Calls classes from actual method_1 and method_2 source code

# FUTURE:
#     This should probably be refactored to draw from a config.py with paths defined there.

@timer
def method_1_funct(num_decks, random_seed, write_decks_to_file = True, base_path = "./data/method_1/"):
    """
    A function that runs the class DecksInt (method_1).
    The reason for this is so that the wrapper @timer (which works on functions) that runs quantitative tests on our output
    can actually run effectively. 
    Should take in the same parameters as DecksInt (method_1) takes in when being created. 
    Should return the .decks attribute itself, in order for the @timer wrapper to get the memory of that attribute.
    """
    decks = DecksInt(num_decks, random_seed, write_decks_to_file = True, base_path = "./data/method_1/")
    return decks.decks

@timer
def method_2_funct(num_decks, random_seed, write_decks_to_file = True, base_path = "./data/method_2/"):
    """    
    A function that runs the class DecksStr (method_2).
    The reason for this is so that the wrapper (which works on functions) that runs quantitative tests on our output
    can actually run effectively. 
    Should take in the same parameters as DecksStr (method_2) takes in when being created.   
    Should return the .decks attribute itself, in order for the @timer wrapper to get the memory of that attribute.
    """
    decks = DecksStr(num_decks, random_seed, write_decks_to_file = True, base_path = "./data/method_2/")
    return decks.decks