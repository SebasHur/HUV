import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image
from xml.dom.xmlbuilder import Options

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



#Nombre de la Pagina
img1 = Image.open('logo2.png')
st.set_page_config(page_title='Hospital Universitario',page_icon = img1, layout='wide',initial_sidebar_state='collapsed')
#import df
data1_unique = pd.read_csv('facturas unicas.csv',sep=",")

#Creacion colummas
data1_unique[['fecha actividad','fecha ingreso','fecha egreso','Fecha de nacimiento']] = data1_unique[['fecha actividad','fecha ingreso','fecha egreso','Fecha de nacimiento']].apply(pd.to_datetime,format='%Y/%m/%d' ,errors='coerce')
data1_unique['Hosp_Days'] = (data1_unique['fecha egreso'] - data1_unique['fecha ingreso'])/np.timedelta64(1,'D')
Mujeres = data1_unique.groupby('genero - sexo').get_group('F')
Hombres = data1_unique.groupby('genero - sexo').get_group('M')

#Sidebar Menu
menu = ['HOME','EDA','PREDICTION','ABOUT']
choice = st.sidebar.selectbox('MENU',menu)
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
                        <td style="width: 450.8pt;border: 1pt solid windowtext;background: rgb(142, 170, 219);padding: 0cm 5.4pt;vertical-align: top;">
                            <p style="text-align: center;"><span style='font-size: 24px; font-family: "Arial Black", sans-serif; color: white;'><strong>HOSPITAL UNIVERSITARIO DEL VALLE</strong></span></p>
                        </td>
                    </tr>
                </tbody>
            </table>""")
    st.title('SIDEBAR MENU')
    stc.html("""<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>The University Hospital del Valle must attend a large population of victims of trauma; only 7081 in 2012. This population generates a high cost for the health system, so the hospital is interested in knowing this population and its behavior over the last 5 years. It is expected to know the costs that these generate to the health system and to be able to create proposals of programs for the promotion and prevention of violence.</p>""")
    stc.html('''<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'><strong><span style="font-size: 20px; line-height: 107%; color: rgb(143, 170, 220);">GRAPHICAL APPROACH TO PATIENT BEHAVIOR</span></strong></p>
            <p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>We invite you to navigate in the side menu to view the graphical statistics of the patients in our EDA. &nbsp;</p>''')
    stc.html('''<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'><strong><span style="font-size: 20px; line-height: 107%; color: rgb(143, 170, 220);">MAKE A COST PREDICTION</span></strong></p>
            <p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>We invite you to make a prediction of the cost of a patient by providing us with basic patient data in our prediction menu.&nbsp;</p>''')
    stc.html('''<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'><strong><span style="font-size: 20px; line-height: 107%; color: rgb(143, 170, 220);">MEET THE TEAM MEMBERS</span></strong></p>
            <p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>Additionally you will be able to know who is the team behind this project by visiting our about menu.</p>''')

elif choice == 'EDA':
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
    # Primera Linea
    row2_1, row2_2, row2_3, row2_4 = st.columns((1,1,1,1))

    with row2_1:
        Female = st.checkbox('FEMALE')
        Male = st.checkbox('MALE')
    with row2_2:
        if (Female is True and Male is True) or (Female is False and Male is False):
            st.subheader('UNIQUE PATIENTS')
            PatientsAll = data1_unique['numero de identificacion del paciente'].nunique()
            st.header(PatientsAll)
        elif Female is True:
            st.subheader('UNIQUE PATIENTS')
            PatientsFemale = data1_unique[data1_unique['genero - sexo']=='F']['numero de identificacion del paciente'].nunique()
            st.header(PatientsFemale)
        elif Male is True:
            st.subheader('UNIQUE PATIENTS')
            PatientsFemale = data1_unique[data1_unique['genero - sexo']=='M']['numero de identificacion del paciente'].nunique()
            st.header(PatientsFemale)
    with row2_3:
        if (Female is True and Male is True) or (Female is False and Male is False):
            st.subheader('TOTAL VISITS')
            InvoicesAll = data1_unique['Numero factura fiscal'].nunique()
            st.header(InvoicesAll)
        elif Female is True:
            st.subheader('TOTAL VISITS')
            InvoicesAll = data1_unique[data1_unique['genero - sexo']=='F']['Numero factura fiscal'].nunique()
            st.header(InvoicesAll)
        elif Male is True:
            st.subheader('TOTAL VISITS')
            InvoicesAll = data1_unique[data1_unique['genero - sexo']=='M']['Numero factura fiscal'].nunique()
            st.header(InvoicesAll)
    with row2_4:
        if (Female is True and Male is True) or (Female is False and Male is False):
            st.subheader('AVERAGE DAYS')
            st.header(round(data1_unique.groupby('genero - sexo')['Hosp_Days'].get_group('M').append(data1_unique.groupby('genero - sexo')['Hosp_Days'].get_group('F')).mean(),2))  
        elif Female is True:
            st.subheader('AVERAGE DAYS')
            st.header(round(data1_unique.groupby('genero - sexo')['Hosp_Days'].get_group('F').mean(),2))
        elif Male is True:
            st.subheader('AVERAGE DAYS')
            st.header(round(data1_unique.groupby('genero - sexo')['Hosp_Days'].get_group('M').mean(),2))
    #graficos
    row3_1, row3_2, row3_3 = st.columns((1,1,1))
    with row3_1:
        st.header('GENDERS BY YEAR')
        fig = px.sunburst(data1_unique, path=['año factura fiscal', 'genero - sexo'])
        fig.update_traces(textinfo="label+percent parent")
        st.plotly_chart(fig, use_container_width=True)
        
    with row3_2:
        st.header('TOP 5 ENTRANCE DIAGNOSIS')
        a = 5
        if (Female is True and Male is True) or (Female is False and Male is False):
            DX_total = data1_unique.groupby('cie10 egrdin').size().to_frame(name='count').reset_index().sort_values(['count'], ascending=False).head(a)
            fig1 = go.Figure(go.Funnel(y = DX_total['cie10 egrdin'],x = DX_total['count'],textposition = "inside",textinfo = "label"))
            fig1.update_yaxes(showticklabels=False)
            fig1.update_layout(font_size=10)
            st.plotly_chart(fig1, use_container_width=True)
        elif Female is True:
            DX_Mujeres = Mujeres.groupby('cie10 egrdin').size().to_frame(name='count').reset_index().sort_values(['count'], ascending=False).head(a)
            fig1 = go.Figure(go.Funnel(y = DX_Mujeres['cie10 egrdin'],x = DX_Mujeres['count'],textposition = "inside",textinfo = "label"))
            fig1.update_yaxes(showticklabels=False)
            fig1.update_layout(font_size=10)
            st.plotly_chart(fig1, use_container_width=True)
        elif Male is True:
            DX_Hombres = Hombres.groupby('cie10 egrdin').size().to_frame(name='count').reset_index().sort_values(['count'], ascending=False).head(a)
            fig1 = go.Figure(go.Funnel(y = DX_Hombres['cie10 egrdin'],x = DX_Hombres['count'],textposition = "inside",textinfo = "label"))
            fig1.update_yaxes(showticklabels=False)
            fig1.update_layout(font_size=14)
            st.plotly_chart(fig1, use_container_width=True)
elif choice == 'PREDICTION':
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
elif choice == 'ABOUT':
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
