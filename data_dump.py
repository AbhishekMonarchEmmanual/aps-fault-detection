import pymongo
import pandas as pd
import json
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

Data_file_path = '/config/workspace/aps_failure_training_set1.csv'
# Database Name
dataBase = "aps"

# Collection  Name
collection = 'sensor'

if __name__ =='__main__':
    df = pd.read_csv(Data_file_path)
    print(f"Rows and columns: {df.shape}")
    df.isnull()
    # convert dataframe to json so that we can dump in mongodb
    df.reset_index(drop= True, inplace= True)
    # df.T to transpose the data which is required.
   
    json_record= list(json.loads(df.T.to_json()).values())
    
    print(json_record[0])

    # insert the data into the mongo db 

    client[dataBase][collection].insert_many(json_record)
    






























    