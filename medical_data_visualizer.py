import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")
df.info()

# 2
convert_meter = df["height"]/ 100
df['overweight'] = np.where((df["weight"] / np.square(convert_meter)) > 25,1,0)

# 3
df["cholesterol"] = df["cholesterol"].map({1:0,2:1,3:1})
df["gluc"] = df["gluc"].map({1:0,2:1,3:1})
df = df.rename(columns = {"sex":"gender"})

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars = ["cardio"],value_vars= ["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    
    # 6
    df_cat =df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
  

    # 7
    

    # 8
    fig  = sns.catplot(
    data=df_cat, 
    x='variable', 
    y='total', 
    hue='value', 
    col='cardio', 
    kind='bar'
).fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= df['height'].quantile(0.025)) & 
    (df['height'] <= df['height'].quantile(0.975)) & 
    (df['weight'] >= df['weight'].quantile(0.025)) & 
    (df['weight'] <= df['weight'].quantile(0.975))
]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # 14
    fig, ax = plt.subplots(figsize=(12, 12))
    
    # 16
    sns.heatmap(
    corr, mask=mask, annot=True, fmt='.1f',center=0, vmin=-0.1, vmax=0.3,square=True, linewidths=.5,cbar_kws={"shrink": .5}
)


    # 16
    fig.savefig('heatmap.png')
    return fig

