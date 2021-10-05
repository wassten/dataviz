import streamlit as st
import numpy as np
import pandas as pd 
import time
import matplotlib.pyplot as plt 

import seaborn as sns

from functools import wraps
from time import time
x= open("time.txt","w+")
def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print ('Temps écoulé : {}'.format((end-start)*1000) + " ms")
        x.write(str(end-start))
        x.write(" seconde(s)")
        x.close()
        return result  
    return wrapper

@timing
def histo(titre, df, b, rw, r, fig,titre2,colums):
    st.title(titre)
    df[[colums]].plot.hist(bins=b, rwidth= rw,range=r, figsize=fig,title= titre2)
    st.pyplot()
    
@timing    
def write_head(df):
    st.write(df.head())
def get_dom(dt):
    return dt.day
def get_weekday(dt):
    return dt.weekday()
def get_hour(df): 
    return df.hour   
def count_rows(rows):
    return len(rows)

@timing
def main():
    x = st.sidebar.selectbox(
    'Choix de la Databases',
    ('uber data', 'ny data')
    )

    if x == 'uber data':
        st.title('Uber')
        st.write('Examining Uber pickups over the time in one day')
        df = pd.read_csv('uber-raw-data-apr14.csv', delimiter=',')

        agree = st.checkbox("Voir Aperçu database")
        if agree:
            write_head(df)

        df['Date/Time'] = pd.to_datetime(df['Date/Time'])
        df['Date/Time'].apply(get_dom)
        df['day'] = df['Date/Time'].map(get_dom)
        df['weekday']=df['Date/Time'].map(get_weekday)
        df['hour'] = df['Date/Time'].map(get_hour)

        histo('Fréquence de course par jour sur une semaine', df, 30, 0.8,(0.5,30.5), (30,15),"Pick - Fréquence des course par jour - Uber - April 2014","day")
        histo('Fréquence de course par jour en un mois', df, 7, 0.8,(-.5, 6.5), None,'Frequency by Hour - Uber - April 2014',"weekday")

    if x == 'ny data':
        st.title('Ny Trips')
        st.write('Examining Uber pickups over the time in New York City')
        dff = pd.read_csv("ny-trips-data.csv")
        dff['tpep_pickup_datetime']=pd.to_datetime(dff["tpep_pickup_datetime"])
        dff['tpep_dropoff_datetime']=pd.to_datetime(dff["tpep_dropoff_datetime"])
        dff['hour'] = dff['tpep_pickup_datetime'].map(get_hour)
        st.title('Trips by hour') 
        dff[["hour"]].plot.hist(bins=24, range=(-0.5,23.5), rwidth=0.9, grid=False)
        
        st.pyplot()

main()



st.write('Made with ❤ at Efrei Paris')

