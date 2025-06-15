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

            df["length"]=df["linecount"].apply(self.categorize_length)
            all_tags=df['tags'].apply(lambda x:x).sum()
            self.unique_tags=set(list(all_tags))
            self.df=df
        
    def categorize_length(self, line_count):
        if (line_count <3):
            return "Short"
        elif (5<=line_count <=10):
            return "Medium"
        else:
            return "Long"
        
    def get_tags(self):
        return self.unique_tags
    def get_filtered_posts(self,length,language,tag):
        df_filtered=self.df[
        (self.df['language']==language )&
        (self.df['length']==length)&
        (self.df['tags'].apply(lambda tags:tag in tags))


        
        
        ]

        return df_filtered.to_dict(orient="records")        
    
    def get_authors(self):
        return sorted(self.df["author"].unique())

    
            
if __name__=="__main__":
    fs=Few_Shots_Post()
    posts=fs.get_filtered_posts("Short","Hinglish","growth")
    print(posts)
            