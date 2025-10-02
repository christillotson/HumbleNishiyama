import os
import sqlite3
import numpy as np
import pandas as pd

import HumbleNishiyama

def read_db() -> pd.DataFrame:

    path_string = os.path.join('database','HN_DB')

    data_path = "./empty_hn_data.csv" # just including because data_DF required
    empty_df = pd.read_csv(data_path)

    table_name_constant = ['tScore']

    table_create_constant = [
    """
    CREATE TABLE tScore ( 
        p1choice TEXT NOT NULL,
        p2choice TEXT NOT NULL,
        p1_win_cards INTEGER NOT NULL,
        p2_win_cards INTEGER NOT NULL,
        draw_cards INTEGER NOT NULL,
        p1_win_tricks INTEGER NOT NULL,
        p2_win_tricks INTEGER NOT NULL,
        draw_tricks INTEGER NOT NULL,
        times_run INTEGER NOT NULL,
        PRIMARY KEY (p1choice, p2choice)
    )
    ;"""
    ]

    db = HumbleNishiyama.HNDB(
        path = path_string,
        data_DF = empty_df,
        create = False,
        load_new_data = False,
        list_of_table_names_constant=table_name_constant,
        list_of_create_sqls_constant=table_create_constant
        )

    sql = """
    SELECT * FROM tScore
    ;"""

    pd.set_option('display.max_rows', 100) # max just needs to be higher than 56 data + 1 column that is going on for this implementation
    
    query_run = db.run_query(sql)

    return(query_run)