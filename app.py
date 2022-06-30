from xml.dom.xmlbuilder import Options
import streamlit as st
from PIL import Image

#Nombre de la Pagina
img = Image.open('logo2.png')
st.set_page_config(page_title='Hospital Universitario', layout='wide',initial_sidebar_state='collapsed')

#Select/Multiple Select

my_lang = ['Python','R','Sql']
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
