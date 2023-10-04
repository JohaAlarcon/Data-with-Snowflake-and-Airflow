import pandas as pd
import time
import random
import os
import re
from datetime import datetime

def get_data (url,liga):

    tiempo =[1,3,2]
    time.sleep (random.choice(tiempo))

    df = pd.read_html(url)
    df = pd.concat([df[0],df[1]], ignore_index = True, axis=1)

    df = df.rename (columns ={0:'Equipo', 1:'J', 2:'G', 3:'E', 4:'P', 5:'GF', 6:'GC', 7:'DIF', 8:'PTS' })

    remove_leading_digits_and_uppercase_except_last = lambda x: re.sub(r'^\d+|[A-Z](?=[A-Z])|[A-Z](?=$)','',x)
    df['Equipo'] = df['Equipo'].apply(remove_leading_digits_and_uppercase_except_last)

    df ['LIGA'] = liga

    run_date = datetime.now()
    run_date = run_date.strftime ("%Y- %m %d")

    df ['CREATE_AT'] = run_date

    return df 