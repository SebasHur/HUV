
import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image
from xml.dom.xmlbuilder import Options
from eps import run_EDA_eps
from patients_genders import run_patients_gender
from about import run_about
from prediction import run_prediction
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from plotly import graph_objects as go
# import pprint


# import json


# from plotly.subplots import make_subplots
# from wordcloud import WordCloud
# from nltk import word_tokenize
# import nltk
# from scipy import stats
# import scipy
# import statsmodels.api as sm

def main():

    #Nombre de la Pagina
    img1 = Image.open('logo2.png')
    st.set_page_config(page_title='Hospital Universitario',page_icon = img1, layout='wide',initial_sidebar_state='expanded')

    #import df
    data1_unique = pd.read_csv('facturas unicas.csv',sep=",")
    data1_unique['cie10 egrdin'] = data1_unique['cie10 egrdin'].str.replace('�','Ñ')
    data1_unique['responsable EPS'] = data1_unique['responsable EPS'].str.replace('�','Ñ')
    EPS = pd.read_pickle('eps_med1' + '.pkl', compression='bz2')

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

        
    def Grouped_Age_gender():
        Gender_Age = data1_unique[['genero - sexo','Age']]
        age_groups = pd.cut(Gender_Age['Age'], bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,np.inf])
        Grouped_Age_gender = pd.crosstab(age_groups, Gender_Age['genero - sexo']).reset_index()
        Grouped_Age_gender['F'] = Grouped_Age_gender['F'] * -1
        Grouped_Age_gender['Age'] = Grouped_Age_gender['Age'].astype(str)
        Grouped_Age_gender['Age'] = Grouped_Age_gender['Age'].replace(',','-',regex=True)
        Grouped_Age_gender['Age'] = Grouped_Age_gender['Age'].replace('\(','',regex=True)
        Grouped_Age_gender['Age'] = Grouped_Age_gender['Age'].replace(']','',regex=True)
        return Grouped_Age_gender

    #Sidebar Menu
    st.sidebar.image('logo-HU_Horizontal_Azul.png')
    menu = ['HOME','EDA','PREDICTION','ABOUT']
    choice = st.sidebar.selectbox('SELECT AN OPTION',menu)
    #Titulo 
    if choice == 'HOME':
        row1_1, row1_2 = st.columns((1, 6))
        img2 = Image.open('logo.png')
        with row1_1:
            st.image(img2, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        with row1_2:
            stc.html("""<table style="background: rgb(47, 84, 150); border-collapse: collapse; border: none; margin-right: calc(3%); width: 97%;">
                    <tbody>
                        <tr>
                            <td style="width: 450.8pt;border: 1pt solid windowtext;background: rgb(84, 172, 210);padding: 0cm 5.4pt;vertical-align: top;">
                                <p style="text-align: center;"><span style='font-size: 24px; font-family: "Arial Black", sans-serif; color: white;'><strong>HOSPITAL UNIVERSITARIO DEL VALLE</strong></span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>""")
        stc.html('''<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>The University Hospital del Valle must attend a large population of victims of trauma; only 7081 in 2012. This population generates a high cost for the health system, so the hospital is interested in knowing this population and its behavior over the last 5 years. It is expected to know the costs that these generate to the health system and take decisions base on the trauma population.</p>
                    <p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size:32px;line-height:107%;color:#00B050;">SIDEBAR MENU</span></p>
                    <div style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>
                        <ul style="margin-bottom:0cm;list-style-type: disc;">
                            <li style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'><strong><span style="line-height:107%;color:#8FAADC;font-size:12.0pt;color:#8FAADC;">GRAPHICAL APPROACH TO PATIENT BEHAVIOR</span></strong></li>
                        </ul>
                    </div>
                    <p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>We invite you to navigate in the side menu to view the graphical statistics of the patients in our EDA.&nbsp;</p>
                    <p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>&nbsp;</p>
                    <div style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>
                        <ul style="margin-bottom:0cm;list-style-type: disc;">
                            <li style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'><strong><span style="line-height:107%;color:#8FAADC;font-size:12.0pt;color:#8FAADC;">MAKE A COST PREDICTION</span></strong></li>
                        </ul>
                    </div>
                    <p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>We invite you to make a prediction of the cost of a patient by providing us with basic patient data in our prediction menu.&nbsp;</p>
                    <p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>&nbsp;</p>
                    <div style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>
                        <ul style="margin-bottom:0cm;list-style-type: disc;">
                            <li style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'><strong><span style="line-height:107%;color:#8FAADC;font-size:12.0pt;color:#8FAADC;">MEET THE TEAM MEMBERS</span></strong></li>
                        </ul>
                    </div>
                    <p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>Additionally you will be able to know who is the team behind this project by visiting our about menu.</p>
                    <p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'><br></p>''',
                    height=700)
    elif choice == 'EDA':
        EDA_OPT = st.sidebar.radio('Select what you want to explore',('Patients and Gender','EPS'))
        if EDA_OPT == 'Patients and Gender':
            run_patients_gender(data1_unique, Mujeres, Hombres, Grouped_Age_gender)
        
        elif EDA_OPT == 'EPS':
            run_EDA_eps(data1_unique,EPS)
    
    elif choice == 'PREDICTION':
        run_prediction()

        
    elif choice == 'ABOUT':
        run_about()
    
if __name__ == '__main__':
    main()
