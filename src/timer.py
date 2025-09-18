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
        time_taken = t1 - t0 # this is in seconds

        # need to calculate path based on specific values passed
        full_data_path = os.path.join(base_path, f"{num_decks}_decks_seed_{random_seed}")
        
        total_size = sum(entry.stat().st_size for entry in os.scandir(full_data_path) if entry.is_file())

        print(f"Ran for {time_taken:.6f} sec(s)")

        # Write header only if file doesn’t exist or is empty
        need_header = not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0
        with open(LOG_FILE, "a", encoding="utf-8") as fh:
            if need_header:
                fh.write("num_decks,random_seed,time_taken,method,storage_size\n")
            fh.write(f"{num_decks},{random_seed},{time_taken:.6f},{fun.__name__},{total_size}\n")

        return results   # return AFTER logging
    
    return _wrapper