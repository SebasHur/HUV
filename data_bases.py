import streamlit as st
import streamlit.components.v1 as stc
import numpy as np
import pandas as pd

def run_data_bases():
    #import df
    data1_unique = pd.read_csv('facturas unicas.csv',sep=",")
    data1_unique['cie10 egrdin'] = data1_unique['cie10 egrdin'].str.replace('�','Ñ')
    data1_unique['responsable EPS'] = data1_unique['responsable EPS'].str.replace('�','Ñ')


    #Creacion colummas
    data1_unique[['fecha actividad','fecha ingreso','fecha egreso','Fecha de nacimiento']] = data1_unique[['fecha actividad','fecha ingreso','fecha egreso','Fecha de nacimiento']].apply(pd.to_datetime,format='%Y/%m/%d' ,errors='coerce')
    data1_unique['Hosp_Days'] = (data1_unique['fecha egreso'] - data1_unique['fecha ingreso'])/np.timedelta64(1,'D')
    data1_unique['Age'] = round((data1_unique['fecha ingreso']-data1_unique['Fecha de nacimiento'])/ np.timedelta64(1, 'Y'),0)
    Mujeres = data1_unique.groupby('genero - sexo').get_group('F')
    Hombres = data1_unique.groupby('genero - sexo').get_group('M')
    data1_unique['WEEK_DAY'] = data1_unique['fecha ingreso'].dt.day_name()
    days = pd.api.types.CategoricalDtype(categories=['Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday','Sunday'], ordered=True)
    data1_unique['WEEK_DAY'] = data1_unique['WEEK_DAY'].astype(days)

    #Limpieza base de datos Columna Responsable EPS
    data1_unique.loc[data1_unique['codigo responsable'] == data1_unique['numero de identificacion del paciente'], 'responsable EPS'] = 'independiente'
    data1_unique.loc[data1_unique['codigo responsable'] == data1_unique['numero de identificacion del paciente'], 'codigo responsable'] = '000'
    count_freq =dict(data1_unique['responsable EPS'].value_counts())
    data1_unique['count_freq'] = data1_unique['responsable EPS']
    data1_unique['count_freq'] = data1_unique['count_freq'].map(count_freq)
    data1_unique.loc[data1_unique['count_freq'] < 100,'responsable EPS'] = 'independiente'
    data1_unique.loc[data1_unique['count_freq'] < 100,'codigo responsable'] = '000'
    count_freq =dict(data1_unique['responsable EPS'].value_counts())
    data1_unique['count_freq'] = data1_unique['responsable EPS']
    data1_unique['count_freq'] = data1_unique['count_freq'].map(count_freq)