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


def run_EDA_eps(data1_unique):
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
    stc.html('''<table style="border-collapse:collapse;border:none;">
                    <tbody>
                        <tr>
                            <td style="width: 1450.8pt; border-collapse: collapse; background: rgb(0, 168, 133); padding: 0cm 5.4pt; vertical-align: middle; text-align: justify;">
                                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><span style="color:white;">TOP EPS (by Patients)</span></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p><br></p>''',height=50)
    # top_EPS = st.slider('',min_value=3, max_value=33, value=10, step=1)
    row2_1, row2_2 = st.columns((2, 1))
    EPS_percent = data1_unique['responsable EPS'].value_counts().rename_axis('EPS').reset_index(name='PATIENTS')
    EPS_percent['PARTICIPATION'] = round((EPS_percent['PATIENTS']/EPS_percent['PATIENTS'].sum())*100,2).astype(float)
    with row2_1:
        fig_EPS_2_1 = go.Figure(go.Funnel(y = EPS_percent['EPS'].head(5),x = EPS_percent['PATIENTS'].head(5),textposition = "inside",textinfo = "label"))
        fig_EPS_2_1.update_yaxes(showticklabels=False)
        fig_EPS_2_1.update_layout(font_size=14)
        fig_EPS_2_1.update_layout(
            margin=dict(l=5, r=5, t=5, b=5),
            paper_bgcolor="LightSteelBlue")
        st.plotly_chart(fig_EPS_2_1, use_container_width=True)
    with row2_2:
        st.dataframe(EPS_percent)
    


