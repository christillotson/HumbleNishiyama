from typing import Callable
from datetime import datetime as dt
import time

SHOW_ARGS = True

def tester(fun: Callable) -> Callable: # call

    def _wrapper(*args, **kwargs):
        
        print(f'{fun.__name__} called with: \n')
        
        if SHOW_ARGS:
            print(f'args: {args}')
            print(f'kwargs: {kwargs}')

        ## args are positional arguments
        ## kwargs are keyword arguments and given specifically

        t0 = dt.now()
        # Always write this like this

        results = fun(*args, **kwargs)

        print(f'Ran for {dt.now()-t0} sec(s)') # so wrapper is a modified version of the function passed in

        # always return the smae thing the function would have
        # i.e., do not modify the return signature 
        
        return results
    
    return _wrapper # debugger returns the wrapper function which is the modified function