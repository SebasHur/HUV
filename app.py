from xml.dom.xmlbuilder import Options
import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px


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
data1_unique = pd.read_csv('facturas unicas.csv',sep=",", 
                 header = True, error_bad_lines=False, index_col=False)
st.dataframe(data1_unique)
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
