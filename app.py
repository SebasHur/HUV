import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image
from xml.dom.xmlbuilder import Options

import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
# import pprint


# import json


# from plotly.subplots import make_subplots
# from wordcloud import WordCloud
# from nltk import word_tokenize
# import nltk
# from scipy import stats
# import scipy
# import statsmodels.api as sm



#Nombre de la Pagina
img1 = Image.open('logo2.png')
st.set_page_config(page_title='Hospital Universitario',page_icon = img1, layout='wide',initial_sidebar_state='collapsed')

#Titulo 
row1_1, row1_2 = st.columns((1, 6))
img2 = Image.open('logo.png')
with row1_1:
    st.image(img2, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
with row1_2:
    stc.html("""<table style="background: rgb(47, 84, 150); border-collapse: collapse; border: none; margin-right: calc(3%); width: 97%;">
            <tbody>
                <tr>
                    <td style="width: 450.8pt;border: 1pt solid windowtext;background: rgb(142, 170, 219);padding: 0cm 5.4pt;vertical-align: top;">
                        <p style="text-align: center;"><span style='font-size: 24px; font-family: "Arial Black", sans-serif; color: white;'><strong>HOSPITAL UNIVERSITARIO DEL VALLE</strong></span></p>
                    </td>
                </tr>
            </tbody>
        </table>""")

#import df
data1_unique = pd.read_csv('facturas unicas.csv',sep=",")

#Creacion colummas
data1_unique[['fecha actividad','fecha ingreso','fecha egreso','Fecha de nacimiento']] = data1_unique[['fecha actividad','fecha ingreso','fecha egreso','Fecha de nacimiento']].apply(pd.to_datetime,format='%Y/%m/%d' ,errors='coerce')
data1_unique['Hosp_Days'] = (data1_unique['fecha egreso'] - data1_unique['fecha ingreso'])/np.timedelta64(1,'D')
Mujeres = data1_unique.groupby('genero - sexo').get_group('F')
Hombres = data1_unique.groupby('genero - sexo').get_group('M')

# Primera Linea
row2_1, row2_2, row2_3 = st.columns((1,2,2))

with row2_1:
    Female = st.checkbox('FEMALE')
    Male = st.checkbox('MALE')
    if (Female is True and Male is True) or (Female is False and Male is False):
        st.subheader('UNIQUE PATIENTS')
        PatientsAll = data1_unique['numero de identificacion del paciente'].nunique()
        st.header(PatientsAll)
        st.subheader('TOTAL VISITS')
        InvoicesAll = data1_unique['Numero factura fiscal'].nunique()
        st.header(InvoicesAll)
        st.subheader('AVERAGE DAYS')
        st.header(round(data1_unique.groupby('genero - sexo')['Hosp_Days'].get_group('M').append(data1_unique.groupby('genero - sexo')['Hosp_Days'].get_group('F')).mean(),2))
        
    elif Female is True:
        st.subheader('UNIQUE PATIENTS')
        PatientsFemale = data1_unique[data1_unique['genero - sexo']=='F']['numero de identificacion del paciente'].nunique()
        st.header(PatientsFemale)
        st.subheader('TOTAL VISITS')
        InvoicesAll = data1_unique[data1_unique['genero - sexo']=='F']['Numero factura fiscal'].nunique()
        st.header(InvoicesAll)
        st.subheader('AVERAGE DAYS')
        st.header(round(data1_unique.groupby('genero - sexo')['Hosp_Days'].get_group('F').mean(),2))
       
    elif Male is True:
        st.subheader('UNIQUE PATIENTS')
        PatientsFemale = data1_unique[data1_unique['genero - sexo']=='M']['numero de identificacion del paciente'].nunique()
        st.header(PatientsFemale)
        st.subheader('TOTAL VISITS')
        InvoicesAll = data1_unique[data1_unique['genero - sexo']=='M']['Numero factura fiscal'].nunique()
        st.header(InvoicesAll)
        st.subheader('AVERAGE DAYS')
        st.header(round(data1_unique.groupby('genero - sexo')['Hosp_Days'].get_group('M').mean(),2))
#graficos
with row2_2:
    st.header('GENDERS BY YEAR')
    fig = px.sunburst(data1_unique, path=['año factura fiscal', 'genero - sexo'])
    fig.update_traces(textinfo="label+percent parent")
    st.plotly_chart(fig, use_container_width=True)
    
with row2_3:
    st.header('ENTRANCE DIAGNOSIS')
    a = 10
    if (Female is True and Male is True) or (Female is False and Male is False):
        DX_total = data1_unique.groupby('cie10 egrdin').size().to_frame(name='count').reset_index().sort_values(['count'], ascending=False).head(a)
        fig1 = go.Figure(go.Funnel(
        y = DX_MUJERES['cie10 egrdin'],
        x = DX_MUJERES['count'],
        textposition = "inside",
        textinfo = "label+value"))
        fig1.update_yaxes(showticklabels=False)
        st.plotly_chart(fig1, use_container_width=True)
    elif Female is True:
        DX_Mujeres = Mujeres.groupby('cie10 egrdin').size().to_frame(name='count').reset_index().sort_values(['count'], ascending=False).head(a)
        fig1 = px.funnel(DX_Mujeres, y='cie10 egrdin', x='count')
        fig1.update_layout(font_size=7)
        st.plotly_chart(fig1, use_container_width=True)
    elif Male is True:
        DX_Hombres = Hombres.groupby('cie10 egrdin').size().to_frame(name='count').reset_index().sort_values(['count'], ascending=False).head(a)
        fig1 = px.funnel(DX_Hombres, y='cie10 egrdin', x='count')
        fig1.update_layout(font_size=7)
        st.plotly_chart(fig1, use_container_width=True)

# with row2_3:
    # Gender_Age = data1_unique[['genero - sexo','Age']]
    # age_groups = pd.cut(Gender_Age['Age'], bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,np.inf])
    # Grouped_Age_gender = pd.crosstab(age_groups, Gender_Age['genero - sexo']).reset_index()
    # Grouped_Age_gender['F'] = Grouped_Age_gender['F'] * -1
    # Grouped_Age_gender['Age'] = Grouped_Age_gender['Age'].astype(str)
    # Grouped_Age_gender['Age'] = Grouped_Age_gender['Age'].replace(',','-',regex=True)
    # Grouped_Age_gender['Age'] = Grouped_Age_gender['Age'].replace('\(','',regex=True)
    # Grouped_Age_gender['Age'] = Grouped_Age_gender['Age'].replace(']','',regex=True)
    # fig, _ = plt.subplots( figsize=(15,5))
    # ax1 = sns.barplot(x='M', y='Age', data=Grouped_Age_gender, palette="Blues")
    # ax2 = sns.barplot(x='F', y='Age', data=Grouped_Age_gender, palette="Greens")
    # plt.title("Population pyramid for Patients")
    # plt.xlabel("Female / Male")
    # plt.xticks(ticks=[-3000,-2000, -1000, 0, 1000, 2000,3000],labels=['3000','2000', '1000', '0', '1000', '2000','3000']);
    # st.plotly_chart(fig)




# my_lang = ['Python','TESTING','Sql']
# choice = st.selectbox('Lenguaje',my_lang)
# st.write('Selecciono{}'.format(choice))

# #multiple selections
# spoken_lang = ('Ingles','Español','Portugues')
# my_spoken = st.multiselect('Spoken Lang', spoken_lang, default='Ingles')

# #slider
# #numeros
# age = st.slider('Age',1,100,5)
# #todos los datos

# color = st.select_slider('Escoge Color', options=['amarillo','azul', 'rojo'])
