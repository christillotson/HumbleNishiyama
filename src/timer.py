from typing import Callable
import time
import inspect
import os
from functools import wraps

SHOW_ARGS = True
LOG_FILE = "wrapper_log.txt"

def timer(fun: Callable) -> Callable:
    sig = inspect.signature(fun)

    @wraps(fun)
    def _wrapper(*args, **kwargs):
        if SHOW_ARGS:
            print(f"{fun.__name__} called with args={args} kwargs={kwargs}")

        t0 = time.time()
        results = fun(*args, **kwargs)   # run function
        t1 = time.time()

        # Bind provided args/kwargs to the function signature
        bound = sig.bind_partial(*args, **kwargs)

        # this is a simple function developed by ChatGPT to get the name of whatever parameters are passed in as a string.
        # the purpose of this 
        def _value_for_param(name: str):
            if name in bound.arguments:
                return bound.arguments[name]
            param = sig.parameters.get(name)
            if param is None:
                return None
            if param.default is inspect._empty:
                return None
            return param.default

        num_decks = _value_for_param("num_decks")
        random_seed = _value_for_param("random_seed")
        base_path = _value_for_param("base_path")
        write_decks_to_file = _value_for_param("write_decks_to_file") # this should be a boolean

        time_taken = t1 - t0 # this is in seconds
        memory = results.nbytes

        # need to calculate path based on specific values passed
        full_data_path = os.path.join(base_path, f"{num_decks}_decks_seed_{random_seed}")
        
        if write_decks_to_file == True:
            total_size = sum(entry.stat().st_size for entry in os.scandir(full_data_path) if entry.is_file())
        else:
            print("WARNING: not writing to file because write_decks_to_file is not True. \n")
            print("Not sure why you'd do something wacky like this,\n")
            print("but for the sake of continuity, the storage size will be set to zero.")
            total_size = 0

        # print(f"Ran for {time_taken:.6f} sec(s)")

        # print(f"Memory size is {results.nbytes}")

        # Write header only if file doesn’t exist or is empty
        need_header = not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0
        with open(LOG_FILE, "a", encoding="utf-8") as fh:
            if need_header:
                fh.write("num_decks,random_seed,method,storage_bytes,memory_bytes,time_taken\n")
            fh.write(f"{num_decks},{random_seed},{fun.__name__},{total_size},{memory},{time_taken:.6f}\n")

        return results   # return AFTER logging
    
    return _wrapper