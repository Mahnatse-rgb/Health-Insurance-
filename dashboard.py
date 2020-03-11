import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns; sns.set(color_codes=True)
import matplotlib.pyplot as plt

########creating table

df = pd.read_csv('/home/recruit/Umuzi/visualization/Insurance-Fees/data/insurance.csv')

#pivot_table = pd.pivot_table(df, index =['age'],columns =[''] )

# new = df['age'].groupby(df['region'])
#
# print(new.head())
# wel  = df[df['region']=='southwest']
# print(wel)

# for a in df['region']:
#     if a == 'southwest':
#
# u = df.groupby(['region', ''])
# print(u.first())

#female = df[df['sex'] == 'female']['charges']

##group gender by charges
a = df.groupby(['sex','charges'])
#-----print(a.first())
be = a.agg({'charges': 'mean'})

print(a.first())
print(be)
# sns.kdeplot(df[df['sex']=='female']['charges'], shade=True, label = 'Female charge')
# plt.show()
