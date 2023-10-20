import pandas as pd
from sklearn.neural_network import MLPClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_object as go 
import plotly.express as px

dataset  =pd.read_csv('projectC234_EPL.csv')
 
goal_columns = dataset['Goals']
sorted = goal_column.groupby(dataset['club'])

sum = sorted.sum()
sorted _goal = sum.sort_values(ascending= False)
print("Premiere League Goals of each club : ", sorted_goal)

epl_top_goals = dataset.sort_values(by = ['Goals'], ascending=False)[:10]
print("Top Goal Scorers : ", epl_top_goals)

fig = px.bar(epl_top_goals, x = 'projectC234_EPL.csv0', y= 'Goals', color='Goals', hover_data=['Club', 'Age'], text='Goals')

fig.show()

