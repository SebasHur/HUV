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


def run_patients_gender(data1_unique, Mujeres, Hombres, Grouped_Age_gender):
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
    # Primera Linea
    row2_1, row2_2, row2_3, row2_4, row2_5, row2_6 = st.columns(6)
    with row2_1:
        stc.html('''<table style="border-collapse:collapse;border:none;">
            <tbody>
                <tr>
                    <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(97, 189, 109); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white">SELECT GENDER</span></p>
                    </td>
                </tr>
            </tbody>
        </table>
        <p><br></p>''',height=50)
        Gender1 = st.radio(label = '', options=('FEMALE','MALE','BOTH'))
    with row2_2:
        stc.html('''<table style="border-collapse:collapse;border:none;">
            <tbody>
                <tr>
                    <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(26, 188, 156); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">PATIENTS</span></p>
                    </td>
                </tr>
            </tbody>
        </table>
        <p><br></p>''', height = 50)
        if Gender1 == 'BOTH':
            PatientsAll = data1_unique['numero de identificacion del paciente'].nunique()
            st.header(f'{PatientsAll:,}')
        elif Gender1 == 'FEMALE':
            PatientsFemale = data1_unique[data1_unique['genero - sexo']=='F']['numero de identificacion del paciente'].nunique()
            st.header(f'{PatientsFemale:,}')
        elif Gender1 == 'MALE':
            PatientsFemale = data1_unique[data1_unique['genero - sexo']=='M']['numero de identificacion del paciente'].nunique()
            st.header(f'{PatientsFemale:,}')
    with row2_3:
        stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(84, 172, 210); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">VISITS</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=50)
        if Gender1 == 'BOTH':
            InvoicesAll = data1_unique['Numero factura fiscal'].nunique()
            st.header(f'{InvoicesAll:,}')
        elif Gender1 == 'FEMALE':
            InvoicesAll = data1_unique[data1_unique['genero - sexo']=='F']['Numero factura fiscal'].nunique()
            st.header(f'{InvoicesAll:,}')
        elif Gender1 == 'MALE':
            InvoicesAll = data1_unique[data1_unique['genero - sexo']=='M']['Numero factura fiscal'].nunique()
            st.header(f'{InvoicesAll:,}')
    with row2_4:
        stc.html('''<table style="border-collapse:collapse;border:none;">
                <tbody>
                    <tr>
                        <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(44, 130, 201); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                            <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">CLINIC DAYS AVERAGE</span></p>
                        </td>
                    </tr>
                </tbody>
            </table>
            <p><br></p>''',height=50)
        if Gender1 == 'BOTH':
            st.header(round(data1_unique.groupby('genero - sexo')['Hosp_Days'].get_group('M').append(data1_unique.groupby('genero - sexo')['Hosp_Days'].get_group('F')).mean(),2))  
        elif Gender1 == 'FEMALE':
            st.header(round(data1_unique.groupby('genero - sexo')['Hosp_Days'].get_group('F').mean(),2))
        elif Gender1 == 'MALE':
            st.header(round(data1_unique.groupby('genero - sexo')['Hosp_Days'].get_group('M').mean(),2))
    with row2_5:
        stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(147, 101, 184); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">INVOICE AVERAGE</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=50)
        if Gender1 == 'BOTH':
            a = round(data1_unique.groupby('genero - sexo')['valor factura fiscal'].get_group('M').append(data1_unique.groupby('genero - sexo')['valor factura fiscal'].get_group('F')).mean(),0).astype(int)
            st.header(f'{a:,}')  
        elif Gender1 == 'FEMALE':
            a = round(data1_unique.groupby('genero - sexo')['valor factura fiscal'].get_group('F').mean(),0).astype(int)
            st.header(f'{a:,}')
            
        elif Gender1 == 'MALE':
            a = round(data1_unique.groupby('genero - sexo')['valor factura fiscal'].get_group('M').mean(),0).astype(int)
            st.header(f'{a:,}')
    with row2_6:
        stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(226, 80, 65); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">TOTAL INVOICES</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=50)
        if Gender1 == 'BOTH':
            a = round(data1_unique.groupby('genero - sexo')['valor factura fiscal'].get_group('M').append(data1_unique.groupby('genero - sexo')['valor factura fiscal'].get_group('F')).sum(),0).astype(int)
            st.header(f'{a:,}')  
        elif Gender1 == 'FEMALE':
            a = round(data1_unique.groupby('genero - sexo')['valor factura fiscal'].get_group('F').sum(),0).astype(int)
            st.header(f'{a:,}')
            
        elif Gender1 == 'MALE':
            a = round(data1_unique.groupby('genero - sexo')['valor factura fiscal'].get_group('M').sum(),0).astype(int)
            st.header(f'{a:,}')
    #graficos
    row4_1, row4_2 = st.columns((1,1))
    with row4_2:
        stc.html('''<table style="border-collapse:collapse;border:none;">
            <tbody>
                <tr>
                    <td style="width: 1450.8pt; border-collapse: collapse;background: rgb(84, 172, 210);padding: 0cm 5.4pt;vertical-align: top;">
                        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">PATIENTS BY YEAR AND MONTH</span></p>
                    </td>
                </tr>
            </tbody>
        </table>''',height=50)
        if Gender1 == 'BOTH':
            by_month1 = data1_unique['fecha ingreso'].dt.to_period('m').value_counts().sort_index()
            by_month1.index = pd.PeriodIndex(by_month1.index)
            df_month = by_month1.rename_axis('month').reset_index(name='PATIENTS')
            df_month =df_month[df_month['month']>='2018-01']
            df_month["months"] = df_month["month"].dt.strftime('%m')
            df_month["years"] = df_month["month"].dt.strftime('%y')
            fig4_1 = px.line(df_month, x='months', y='PATIENTS', color='years',range_x=(0,11))
            fig4_1.update_layout(margin=dict(l=5, r=5, t=5, b=5))
            st.plotly_chart(fig4_1, use_container_width=True)
        elif Gender1 == 'FEMALE':
            by_month1 = Mujeres['fecha ingreso'].dt.to_period('m').value_counts().sort_index()
            by_month1.index = pd.PeriodIndex(by_month1.index)
            df_month = by_month1.rename_axis('month').reset_index(name='PATIENTS')
            df_month =df_month[df_month['month']>='2018-01']
            df_month["months"] = df_month["month"].dt.strftime('%m')
            df_month["years"] = df_month["month"].dt.strftime('%y')
            fig4_1 = px.line(df_month, x='months', y='PATIENTS', color='years',range_x=(0,11))
            fig4_1.update_layout(margin=dict(l=5, r=5, t=5, b=5))
            st.plotly_chart(fig4_1, use_container_width=True)
        elif Gender1 == 'MALE':
            by_month1 = Hombres['fecha ingreso'].dt.to_period('m').value_counts().sort_index()
            by_month1.index = pd.PeriodIndex(by_month1.index)
            df_month = by_month1.rename_axis('month').reset_index(name='PATIENTS')
            df_month =df_month[df_month['month']>='2018-01']
            df_month["months"] = df_month["month"].dt.strftime('%m')
            df_month["years"] = df_month["month"].dt.strftime('%y')
            fig4_1 = px.line(df_month, x='months', y='PATIENTS', color='years',range_x=(0,11))
            fig4_1.update_layout(margin=dict(l=5, r=5, t=5, b=5))
            st.plotly_chart(fig4_1, use_container_width=True)
    with row4_1:
        stc.html('''<table style="border-collapse:collapse;border:none;">
            <tbody>
                <tr>
                    <td style="width: 1450.8pt; border-collapse: collapse;background: rgb(84, 172, 210);padding: 0cm 5.4pt;vertical-align: top;">
                        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">TOP 5 ENTRANCE DIAGNOSE</span></p>
                    </td>
                </tr>
            </tbody>
        </table>''',height=50)
        a = 5
        if Gender1 == 'BOTH':
            DX_total = data1_unique.groupby('cie10 egrdin').size().to_frame(name='count').reset_index().sort_values(['count'], ascending=False).head(a)
            fig1 = go.Figure(go.Funnel(y = DX_total['cie10 egrdin'],x = DX_total['count'],textposition = "inside",textinfo = "label"))
            fig1.update_yaxes(showticklabels=False)
            fig1.update_layout(font_size=14)
            fig1.update_layout(margin=dict(l=5, r=5, t=5, b=5))
            st.plotly_chart(fig1, use_container_width=True)
        elif Gender1 == 'FEMALE':
            DX_Mujeres = Mujeres.groupby('cie10 egrdin').size().to_frame(name='count').reset_index().sort_values(['count'], ascending=False).head(a)
            fig1 = go.Figure(go.Funnel(y = DX_Mujeres['cie10 egrdin'],x = DX_Mujeres['count'],textposition = "inside",textinfo = "label"))
            fig1.update_yaxes(showticklabels=False)
            fig1.update_layout(font_size=14)
            fig1.update_layout(margin=dict(l=5, r=5, t=5, b=5))
            st.plotly_chart(fig1, use_container_width=True)
        elif Gender1 == 'MALE':
            DX_Hombres = Hombres.groupby('cie10 egrdin').size().to_frame(name='count').reset_index().sort_values(['count'], ascending=False).head(a)
            fig1 = go.Figure(go.Funnel(y = DX_Hombres['cie10 egrdin'],x = DX_Hombres['count'],textposition = "inside",textinfo = "label"))
            fig1.update_yaxes(showticklabels=False)
            fig1.update_layout(font_size=14)
            fig1.update_layout(margin=dict(l=5, r=5, t=5, b=5))
            st.plotly_chart(fig1, use_container_width=True)
    row3_1, row3_2 = st.columns((1,2))
    with row3_1:
        stc.html('''<table style="border-collapse:collapse;border:none;">
            <tbody>
                <tr>
                    <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(44, 130, 201); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">GENDER BY YEAR</span></p>
                    </td>
                </tr>
            </tbody>
        </table>
        <p><br></p>''',height=50)
        fig = px.sunburst(data1_unique, path=['año factura fiscal', 'genero - sexo'])
        fig.update_traces(textinfo="label+percent parent")
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig, use_container_width=True) 
    with row3_2:
        stc.html('''<table style="border-collapse:collapse;border:none;">
            <tbody>
                <tr>
                    <td style="width: 1450.8pt; border-collapse: collapse;background: rgb(84, 172, 210);padding: 0cm 5.4pt;vertical-align: top;">
                        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">AGE DISTRIBUTION BY GENDER</span></p>
                    </td>
                </tr>
            </tbody>
        </table>''',height=50)
        Grouped_Age_gender = Grouped_Age_gender()
        y_age = Grouped_Age_gender['Age']
        x_M = Grouped_Age_gender['M']
        x_F = Grouped_Age_gender['F']
        # Creating instance of the figure
        fig4_2 = go.Figure()
        
        # Adding Male data to the figure
        fig4_2.add_trace(go.Bar(y= y_age, x = x_M, name = 'Male', orientation = 'h'))
        
        # Adding Female data to the figure
        fig4_2.add_trace(go.Bar(y = y_age, x = x_F,name = 'Female', orientation = 'h'))
        fig4_2.update_layout(barmode = 'relative',
                        bargap = 0.0, bargroupgap = 0,
                        xaxis = dict(tickvals = [-3000, -2000, -1000,0, 1000, 2000,3000],                                
                                    ticktext = ['3000', '2000', '1000', '0', '1000', '2000', '3000'])
                        )
        fig4_2.update_xaxes(tickvals=[-3000, -2000, -1000,0, 1000, 2000,3000])
        fig4_2.update_layout(margin=dict(l=5, r=5, t=5, b=5))
        st.plotly_chart(fig4_2, use_container_width=True)
    stc.html('''<table style="border-collapse:collapse;border:none;">
            <tbody>
                <tr>
                    <td style="width: 1450.8pt; border-collapse: collapse;background: rgb(147, 101, 184);padding: 0cm 5.4pt;vertical-align: top;">
                        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">PARTICIPATION BY DIAGNOSIS</span></p>
                    </td>
                </tr>
            </tbody>
        </table>''',height=50)
    #multiple selections
    diagnosticos = (data1_unique['cie10 egrdin'].unique())
    Chose_Diag = st.multiselect('Select diagnose (you can choose more than one)', diagnosticos)
    row5_1,row5_2,row5_3 = st.columns(3)
    row6_1,row6_2,row6_3 = st.columns(3)
    if Chose_Diag == []:
        pass
    else:
        # st.write(Chose_Diag)
        Diag_5 = pd.concat([data1_unique.groupby('cie10 egrdin').get_group(name) for name in Chose_Diag])
        
        # st.table(Diag_5)
        with row5_2:
            stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(97, 189, 109); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">PATIENTS AGE</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=50)
            fig_row_5_1 = plt.figure()
            sns.histplot(Diag_5 , x='Age',kde=True, hue='genero - sexo')
            st.pyplot(fig_row_5_1)
        with row5_3:
            stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(0, 168, 133); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">CLINIC DAYS</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=50)
            fig_row_5_2 = plt.figure()
            sns.histplot(Diag_5 , x='Hosp_Days',kde=True, hue='genero - sexo')
            st.pyplot(fig_row_5_2)
        with row6_3:
            stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(235, 107, 86); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">INVOICE</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=50)
            fig_row_5_2 = plt.figure()
            sns.histplot(Diag_5 , x='valor factura fiscal',kde=True, hue='genero - sexo')
            st.pyplot(fig_row_5_2)
        with row5_1:
            stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(44, 130, 201); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">TOTAL PATIENTS</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=50)
            Patients1 = Diag_5['numero de identificacion del paciente'].nunique()
            st.subheader(f'{Patients1:,}')
            stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(44, 130, 201); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">FEMALE PATIENTS</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=50)
            Patients2 = Diag_5[Diag_5['genero - sexo']=='F']['numero de identificacion del paciente'].nunique()
            st.subheader(f'{Patients2:,}')
            stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(44, 130, 201); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">MALE PATIENTS</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=50)
            Patients3 = Diag_5[Diag_5['genero - sexo']=='M']['numero de identificacion del paciente'].nunique()
            st.subheader(f'{Patients3:,}')
        with row6_1:
            stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(0, 168, 133); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">PATIENTS BY DAY</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=50)
            fig_row_6_1 = plt.figure()
            sns.histplot(Diag_5 , x='WEEK_DAY')
            plt.xticks(rotation=45)
            st.pyplot(fig_row_6_1)

        with row6_2:
            stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(243, 121, 52); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">DEPARTURE REASON</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=50)
            fig_row_6_1 = plt.figure()
            sns.histplot(Diag_5 , x='Causa Egreso')
            plt.xticks(rotation=45)
            st.pyplot(fig_row_6_1)