# Create an empty HN database based on empty_hn_data.csv
import os
import sqlite3
import numpy as np
import pandas as pd

import HumbleNishiyama

def add_new(data_DF:pd.DataFrame
            ) -> None:

    path_string = os.path.join('database','HN_DB')

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
        data_DF = data_DF,
        create = False,
        load_new_data = True,
        list_of_table_names_constant=table_name_constant,
        list_of_create_sqls_constant=table_create_constant
        )
    
    return