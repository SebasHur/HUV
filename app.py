from xml.dom.xmlbuilder import Options
import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image

#Nombre de la Pagina
img1 = Image.open('logo2.png')
st.set_page_config(page_title='Hospital Universitario',page_icon = img1, layout='wide',initial_sidebar_state='collapsed')

#Titulo 
stc.html("""<table style="background: rgb(47, 84, 150); border-collapse: collapse; border: none; margin-right: calc(2%); width: 98%;">
                <tbody>
                    <tr>
                        <td style="width: 450.8pt;border: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                            <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong><span style="font-size:19px;color:#5B9BD5;">HOSPITAL UNIVERSITARIO DEL VALLE</span></strong></p>
                        </td>
                    </tr>
                </tbody>
            </table>""")    

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
