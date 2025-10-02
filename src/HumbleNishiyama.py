from src.base_db_weird_pandas import BaseDB

import os
import sqlite3
import numpy as np
import pandas as pd
import shutil

class HNDB(BaseDB):
        
    def __init__(self,
                 path: str,
                 data_DF:pd.DataFrame = pd.DataFrame(),
                 
                 # this should be a folder, within which will be at least two other folders, 
                 #named to_load and loaded
                 
                 create: bool = False,
                 load_new_data:bool = False,
                 
                 list_of_table_names_constant: list = [],
                 list_of_table_paths_constant: list = [],
                 list_of_create_sqls_constant: list = [],

                ): # need to include this and then call super() to get init for the parent class
        super().__init__(
                        path,
                        data_DF,
                        
                        create,
                        load_new_data,
                        
                        list_of_table_names_constant,
                        list_of_table_paths_constant,
                        list_of_create_sqls_constant,
                    )
    
    def _load_new_data(self) -> None: # I asked ChatGPT to help with this btw
        print('_load_new_data function activated')
    
        try:
            current_pd = self.data_DF
    
            # select the relevant columns
            scores = current_pd[['p1choice', 'p2choice', 'p1_win_cards',
                                 'p2_win_cards', 'draw_cards', 'p1_win_tricks',
                                 'p2_win_tricks', 'draw_tricks',
                                 'times_run']]
    
            # UPSERT statement: if (p1choice,p2choice) already exists, increment counts
            
            sql_upsert = """
            INSERT INTO tScore (p1choice, p2choice, p1_win_cards, p2_win_cards, draw_cards, p1_win_tricks, p2_win_tricks, draw_tricks, times_run)
            VALUES (:p1choice, :p2choice, :p1_win_cards, :p2_win_cards, :draw_cards, :p1_win_tricks, :p2_win_tricks, :draw_tricks, :times_run)
            ON CONFLICT(p1choice, p2choice) DO UPDATE SET
                p1_win_cards = p1_win_cards + excluded.p1_win_cards,
                p2_win_cards = p2_win_cards + excluded.p2_win_cards,
                draw_cards   = draw_cards   + excluded.draw_cards,
                p1_win_tricks= p1_win_tricks+ excluded.p1_win_tricks,
                p2_win_tricks= p2_win_tricks+ excluded.p2_win_tricks,
                draw_tricks  = draw_tricks  + excluded.draw_tricks,
                times_run    = times_run    + excluded.times_run;
            """
    
            # Loop through the dataframe and apply UPSERT
            for _, row in scores.iterrows():
                self.run_action(
                    sql=sql_upsert,
                    params=row.to_dict(),
                    keep_open=True,
                    commit=True
                )
    
            print(f'processed pandas dataframe')
    
        except Exception as e:
            print(f'something went wrong with the dataframe you passed in')
            self._conn.rollback()
            self._close()
            raise
        self._close()
                
        return


        