import pandas as pd
import os 

def preprocess_data(input_path="data/raw_pbp.csv", output_path="data/processed_pbp.csv"):

    print("Loading raw data...")
    df = pd.read_csv(input_path)

    print("Initial shape:", df.shape)
    
    #Keep real players

    df = df[df["play_type"].notna()]
    df =df[df["play_type"].isin(["pass","run"])]

    #Select columns

    columns_to_keep = [
        "posteam",
        "defteam",
        "play_type",
        "yards_gained",
        "down",
        "ydstogo",
        "yardline_100",
        "game_seconds_remaining",
        "score_differential",
        "epa",
    ]


    df = df[columns_to_keep]

    #Handle missing values

    df = df.dropna()



    #Pass indicator
    df["is_pass"] = (df["play_type"]== "pass").astype(int)

    #Red zone indicator 
    df["red_zone"] = (df["yardline_100"] <= 20).astype(int)

    #Late game indicator (last 5 minutes)
    df["late_game"] = (df["game_seconds_remaining"] <=300).astype(int)

    #Play success target
    df["success"] = (df["yards_gained"] > 0).astype(int)

    print("Final shape:",df.shape)

    #Save processed file

    os.makedirs("data",exist_ok=True)
    df.to_csv(output_path,index=False)

    print(f"Processed data saved to {output_path}")

    return df

if __name__ == "__main__":
    preprocess_data()


