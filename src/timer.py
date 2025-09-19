from typing import Callable
import time
import inspect
import os
from functools import wraps

def timer(fun: Callable) -> Callable:
    
    '''
    This is a wrapper designed to be used on method functions, from run_methods_as_functions.py.
    This wrapper
        1. Gets the arguments used, using inspect library
        2. Runs the function, collecting time values before and after
        3. Defines a function to get the values for each parameter 
        4. Runs that function on each parameter we are interested in, to get the values
        5. Calculates time taken (seconds)
        6. Calculates memory (bytes)
        7. Calculates size of data stored, based on a path that is created from the unique parameters passed
        8. Makes the log file and logs this info for each unique parameter combo

    FUTURE:
        This should probably be refactored to draw from a config.py with paths defined there.
        This includes path to data which is calculated here but is also done elsewhere. 
    '''
    
    # This is what is used to later get the arguments
    sig = inspect.signature(fun)

    SHOW_ARGS = False
    LOG_FILE = "./data/wrapper_log.txt"

    # This wrapper of the wrapper ensures that attributes remain the same as the function wrapped, not for _wrapper
    # Specifically, we need this to get the fun.__name__ as method_1_funct or method_2_funct, instead of _wrapper
    @wraps(fun)
    def _wrapper(*args, **kwargs):
        if SHOW_ARGS:
            print(f"{fun.__name__} called with args={args} kwargs={kwargs}")

        # Get initial time, run experiment, then get time when finished
        t0 = time.time()

        # Run function with the specific arguments
        # The function should also return the .decks attribute of the Decks class in order to get memory size of the decks
        results = fun(*args, **kwargs)

        t1 = time.time()

        # Bind provided args/kwargs to the function signature
        bound = sig.bind_partial(*args, **kwargs)

        # This is a simple function developed by ChatGPT to get the name of whatever parameters are passed in as a string.
        # The purpose of all these ifs, is to get the value depending on how it is passed
        # Such as arg, kwarg, as the default, etc
        def _value_for_param(name: str):
            if name in bound.arguments:
                return bound.arguments[name]
            param = sig.parameters.get(name)
            if param is None:
                return None
            if param.default is inspect._empty:
                return None
            return param.default

        # This should be an integer, the number of decks tested
        num_decks = _value_for_param("num_decks")

        # This should be an integer
        random_seed = _value_for_param("random_seed")

        # This should be a string
        base_path = _value_for_param("base_path")

        # This should be a Boolean
        write_decks_to_file = _value_for_param("write_decks_to_file")

        # This is in seconds, the time taken
        time_taken = t1 - t0 

        # This returns a number and is the memory size
        # .nbytes can only be called on a Numpy array
        # It is called on the .decks attribute, a numpy array containing the decks generated from the class
        memory = results.nbytes

        # Need to create path to where data is stored based on specific values passed
        full_data_path = os.path.join(base_path, f"{num_decks}_decks_seed_{random_seed}")
        
        if write_decks_to_file == True:
            total_size = sum(entry.stat().st_size for entry in os.scandir(full_data_path) if entry.is_file())
        else:
            print("WARNING: not writing to file because write_decks_to_file is not True. \n")
            print("Not sure why you'd do something wacky like this,\n")
            print("but for the sake of continuity, the storage size will be set to zero.")
            total_size = 0

        # Make file (and through that, data folder) since data needs to exist for this to work
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        
        # Write header only if is empty
        need_header = not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0
        with open(LOG_FILE, "a", encoding="utf-8") as fh:
            if need_header:
                fh.write("num_decks,random_seed,method,storage_bytes,memory_bytes,time_taken\n")
            fh.write(f"{num_decks},{random_seed},{fun.__name__},{total_size},{memory},{time_taken:.6f}\n")

        return results   # return AFTER logging
    
    return _wrapper