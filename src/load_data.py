import nfl_data_py as nfl 
import pandas as pd 
import os

def load_and_save_data(seasons):
    pbp = nfl.import_pbp_data(seasons)

    #create data folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Saves raw data
    pbp.to_csv("data/raw_pbp.csv", index=False)

    print("Data saved to data/raw_pbp.csv")

    return pbp

if __name__ == "__main__":
    load_and_save_data([2020,2021,2022,2023])