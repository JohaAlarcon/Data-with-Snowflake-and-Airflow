import pandas as pd
import time
import random
import re
from datetime import datetime

def get_data(url,liga):

    tiempo =[1,3,2]
    time.sleep (random.choice(tiempo))

    df = pd.read_html(url, delim_whitespace=True)
    df = pd.concat([df[0],df[1]], ignore_index = True, axis=1)

    df = df.rename (columns ={0:'Equipo', 1:'J', 2:'G', 3:'E', 4:'P', 5:'GF', 6:'GC', 7:'DIF', 8:'PTS' })

    remove_leading_digits_and_uppercase_except_last = lambda x: re.sub(r'^\d+|[A-Z](?=[A-Z])|[A-Z](?=$)','',x)
    df['Equipo'] = df['Equipo'].apply(remove_leading_digits_and_uppercase_except_last)

    df ['LIGA'] = liga

    run_date = datetime.now()
    run_date = run_date.strftime ("%Y- %m %d")

    df ['CREATE_AT'] = run_date

    return df

def data_processing(df):

    df_colombia=get_data(df['URL'][0],df['LIGA'][0])
    df_inglaterra=get_data(df['URL'][1],df['LIGA'][1])
    df_italia=get_data(df['URL'][2],df['LIGA'][2])
    df_alemania=get_data(df['URL'][3],df['LIGA'][3])
    df_francia=get_data(df['URL'][4],df['LIGA'][4])


    df_final=pd.concat([df_colombia,df_inglaterra,df_italia,df_alemania,df_francia],ignore_index=False)

    return df_final