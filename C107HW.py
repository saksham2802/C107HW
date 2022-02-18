import pandas as pd 
import csv 
import plotly.graph_objects as go 
df=pd.read_csv("data.csv")
student_df=df.loc[df['student_id']=="TRL_abc"]
print(student_df.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(x=df.groupby("student_id")['attempt'].mean(),y=['Level1','Level2','Level3','Level4'],orientation='h'))
fig.show()