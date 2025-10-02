# Create an empty HN database based on empty_hn_data.csv
import os
import sqlite3
import numpy as np
import pandas as pd

import HumbleNishiyama

def create_empty() -> None:

    path_string = os.path.join('database','HN_DB')

    if os.path.exists(path_string):
        os.remove(path_string)
        print(f"File '{path_string}' deleted successfully.")
    else:
        print(f"File '{path_string}' does not exist.")

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

    data_path = "./empty_hn_data.csv"
    empty_df = pd.read_csv(data_path)

    db = HumbleNishiyama.HNDB(
        path = path_string,
        data_DF = empty_df,
        create = True,
        load_new_data = True,
        list_of_table_names_constant=table_name_constant,
        list_of_create_sqls_constant=table_create_constant
        )
    return