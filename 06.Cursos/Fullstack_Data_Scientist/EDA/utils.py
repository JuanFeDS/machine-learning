import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

penguin_color = {
    'Adelie': '#1d3461',
    'Gentoo': '#376996',
    'Chinstrap': '#829cbc'
}

def meta_df(df):
    df_meta = pd.DataFrame(df.columns)
    df_meta.columns = ['Variable']
    df_meta['Data_Type'] = df_meta['Variable'].apply(lambda x: str(df[f'{x}'].dtype))
    df_meta['Valores_Nulos'] = df_meta['Variable'].apply(lambda x: len(df[df[f'{x}'].isna()]))
    df_meta['Distinct_Values'] = df_meta['Variable'].apply(lambda x: len(df[f'{x}'].value_counts()))

    return df_meta
    
def count_valores(df, variable):
    df_count = pd.DataFrame(df[variable].value_counts()).reset_index()
    df_count.columns = [variable, 'penguins']
    return df_count

def graph_bar(df, variable):
    fig, ax = plt.subplots(figsize=(14, 5))

    plt.title(
        f'Pinguinos por {variable}', 
        fontweight=1000, 
        size=16, 
        color='white'
    )

    fig.patch.set_facecolor('#21252b') 
    ax.set_facecolor('#282c34') 

    sns.barplot(
        data=df, 
        x=variable, 
        y='penguins',
        palette =list(penguin_color.values())
    )

    plt.xlabel(variable, size=12, weight=700, color='white')
    plt.xticks(color='white', size=12)

    plt.ylabel('Cantidad de Pinguinos', size=12, weight=700, color='white')
    plt.yticks(color='white', size=12)

    plt.show()
    
def proportions_values(df, variable):
    df_proportions = pd.DataFrame(df[variable].value_counts()).reset_index()
    df_proportions.columns = [variable, 'penguins']
    df_proportions['%'] = df_proportions['penguins'].apply(lambda x: round(x/df_proportions['penguins'].sum()*100))
    return df_proportions

def graph_proportions(df, variable):
    fig, ax = plt.subplots(figsize = (1, 5))
    y_offset = -10
    barWidth=0.5

    plt.title(f'Proporción de pinguinos por {variable}', color='white')
    fig.patch.set_facecolor('#21252b') 
    ax.set_facecolor('#282c34') 

    for i in range(len(df)):
        if i == 0:
            plt.bar([1], df['%'][i], color=list(penguin_color.values())[i], width=barWidth, label=df[variable][i])
        else:
            plt.bar([1], df['%'][i], bottom=sum(tuple([df['%'][j] for j in range(i)])), color=list(penguin_color.values())[i], width=barWidth, label=df[variable][i])

    plt.xticks([1], ['Pinguinos'], color='white')

    plt.yticks(color='white')
    plt.ylim(0,100)

    plt.legend(title=variable, bbox_to_anchor=(1.25, 0.7), borderaxespad=0)
    
    for bar in ax.patches:
        if bar.get_height() != 0:
            ax.text(
              bar.get_x() + bar.get_width() / 2,
              bar.get_height() + bar.get_y() + y_offset,
              f'{round(bar.get_height())}%',
              ha='center',
              color='black',
              size=10
          )    

    plt.show()