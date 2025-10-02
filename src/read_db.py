import os
import sqlite3
import numpy as np
import pandas as pd

from src.HumbleNishiyama import HNDB

def read_db() -> pd.DataFrame:

    path_string = os.path.join('src','database','HN_DB')

    db = HNDB(
        path = path_string,
        create = False,
        load_new_data = False,
        )

    sql = """
    SELECT * FROM tScore
    ;"""

    pd.set_option('display.max_rows', 100) # max just needs to be higher than 56 data + 1 column that is going on for this implementation
    
    query_run = db.run_query(sql)

    return(query_run)