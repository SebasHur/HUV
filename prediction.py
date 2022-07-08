import pickle
from numpy import ceil
import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image
from xml.dom.xmlbuilder import Options
import pandas as pd
from aux_pred import *
from datetime import datetime as dt

sampledf = pd.read_csv("Sampledf.csv")
model = pickle.load(open("./model.sav", "rb"))
@st.cache
def run_prediction(unique_pos, unique_eps, unique_cie): 
    with open("pred.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    row1_1, row1_2 = st.columns((1, 6))
    img2 = Image.open('Photos and Logos/logo.png')
    with row1_1:
        st.image(img2, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    with row1_2:
        stc.html("""
        <table style="background: rgb(47, 84, 150); border-collapse: collapse; border: none; margin-right: calc(3%); width: 97%;">
                <tbody>
                    <tr>
                        <td style="width: 450.8pt;border: 1pt solid windowtext;background: rgb(84, 172, 210);padding: 0cm 5.4pt;vertical-align: top;">
                            <p style="text-align: center;"><span style='font-size: 24px; font-family: "Arial Black", sans-serif; color: white;'><strong>HOSPITAL UNIVERSITARIO DEL VALLE</strong></span></p>
                        </td>
                    </tr>
                </tbody>
            </table>""")

    stc.html('''
    <table style="border-collapse:collapse;border:none;">
        <tbody>
            <tr>
                <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(97, 189, 109); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                    <p style='margin-top:0;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white">SELECT DATE OF BIRTH</span></p>
                </td>
            </tr>
        </tbody>
    </table>
    <p><br></p>''',height=25)
    Date = st.date_input("", min_value= dt(dt.now().year - 100, dt.now().month, dt.now().day))
    TransformedDate = pd.to_datetime(Date).toordinal()

    stc.html('''<table style="border-collapse:collapse;border:none;">
        <tbody>
            <tr>
                <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(26, 188, 156); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                    <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">SELECT POS TYPE</span></p>
                </td>
            </tr>
        </tbody>
    </table>
    <p><br></p>''', height = 25)
    Pos = st.selectbox("", unique_pos)

    stc.html('''<table style="border-collapse:collapse;border:none;">
                <tbody>
                    <tr>
                        <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(84, 172, 210); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                            <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">SELECT CIE 10</span></p>
                        </td>
                    </tr>
                </tbody>
            </table>
            <p><br></p>''',height=25)
    cie = st.selectbox("", unique_cie)

    stc.html('''<table style="border-collapse:collapse;border:none;">
            <tbody>
                <tr>
                    <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(44, 130, 201); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">SELECT EPS</span></p>
                    </td>
                </tr>
            </tbody>
        </table>
        <p><br></p>''',height=25)
    Eps = st.selectbox("", unique_eps)
    
    stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(147, 101, 184); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">SELECT GENDER</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''', height = 25)
    Gender = st.selectbox("", "FEMALE MALE".split())

    stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(226, 80, 65); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">PREDICTION</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=25)
    try:
        st.markdown(f'''
        ##### For a {Gender} patient born in {Date} whose EPS is {Eps}, with a CIE 10 of {cie} and POS type {Pos} the predicted cost is''')
        df_to_show = map_to_eps(Eps, sampledf) 
        df_to_show = map_to_pos(Pos, df_to_show) 
        df_to_show = map_to_cie(cie, df_to_show) 
        df_to_show = map_gender(Gender, df_to_show) 
        df_to_show["Fecha de nacimiento"] = TransformedDate
        predicted_value = model.predict(df_to_show)
        st.markdown(f"# {ceil(predicted_value[0])}$")
    except Exception:
        pass
