import os
import sqlite3
import numpy as np
import pandas as pd

from src.HumbleNishiyama import HNDB

def add_new(data_DF:pd.DataFrame
            ) -> None:

    path_string = os.path.join('src','database','HN_DB')

    db = HNDB(
        path = path_string,
        data_DF = data_DF,
        create = False,
        load_new_data = True,
        )
    
    return