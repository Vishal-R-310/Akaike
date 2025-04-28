#Agent for answering basic questions from a CSV File
import pandas as pd
from langchain.chains import LLMChain

#Read dress.csv file
data = pd.read_csv("../data/dress.csv")
print(data.shape)
print(data.columns.tolist())

#Engine 
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine

engine = create_engine("sqlite:///dress.db")
data.to_sql("dress", engine, index=False)

#SQL Query for rating > 4.5
db = SQLDatabase(engine=engine)
print(db.dialect)
print(db.get_usable_table_names())
print(db.run("SELECT Dress_ID FROM dress where Rating>4.5;"))

db = SQLDatabase(engine=engine)
print(db.dialect)
print(db.get_usable_table_names())
print(db.run("SELECT Style, Price, Material FROM dress GROUP BY Style ORDER BY Size DESC LIMIT 5;"))