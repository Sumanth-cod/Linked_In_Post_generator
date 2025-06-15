import json
import pandas as pd
class Few_Shots_Post:
    def  __init__(self, file_path = "data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)

            df=pd.json_normalize(posts)
            self.df=df
            
if __name__=="__main__":
    fs=Few_Shots_Post()
    pass
            