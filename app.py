import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image
from xml.dom.xmlbuilder import Options

import numpy as np
import pandas as pd
import plotly.express as px

# import pprint
# import seaborn as sns
# import matplotlib.pyplot as plt
# import json

# import plotly.graph_objects as go
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

# Primera Linea
row2_1, row2_2, row2_3, row2_4 = st.columns((2,1,1,4))
with row2_1:
    # a = st.radio('Gender',('M','F'))
    Female = st.checkbox('FEMALE')
    Male = st.checkbox('MALE')
    if (Female is True and Male is True) or (Female is False and Male is False):
        st.write('Patient Data')
    if Male == 'hombre':
        st.write('yeap')

    
#graficos
with row2_4:
    # st.write('Distribucion Por Genero')
    fig = px.sunburst(data1_unique, path=['año factura fiscal', 'genero - sexo'], 
                title='Patient Gender')
    fig.update_traces(textinfo="label+percent parent")
    st.plotly_chart(fig)
#Select/Multiple Select


my_lang = ['Python','TESTING','Sql']
choice = st.selectbox('Lenguaje',my_lang)
st.write('Selecciono{}'.format(choice))

#multiple selections
spoken_lang = ('Ingles','Español','Portugues')
my_spoken = st.multiselect('Spoken Lang', spoken_lang, default='Ingles')

#slider
#numeros
age = st.slider('Age',1,100,5)
#todos los datos

color = st.select_slider('Escoge Color', options=['amarillo','azul', 'rojo'])
