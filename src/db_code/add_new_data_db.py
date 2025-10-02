import os
import sqlite3
import numpy as np
import pandas as pd

import HumbleNishiyama

def add_new(data_DF:pd.DataFrame
            ) -> None:

    path_string = os.path.join('database','HN_DB')

    db = HumbleNishiyama.HNDB(
        path = path_string,
        data_DF = data_DF,
        create = False,
        load_new_data = True,
        )
    
    return