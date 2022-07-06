import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image
from xml.dom.xmlbuilder import Options

def run_about():
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
        stc.html('''<p style="text-align: center;"><span style="font-family: Arial, Helvetica, sans-serif; font-size: 28px; color: rgb(84, 172, 210);">TEAM 231 - CORRELATION ONE</span>&nbsp;</p><br>''')
    sp1,row2_1,sp2, row2_2,sp3, row2_3,sp4= st.columns((1,2,1,2,1,2,1))
    sp1, row3_1,sp2, row3_2,sp3, row3_3,sp4= st.columns((1,2,1,2,1,2,1))
    size_image_us = 200
    with row2_1:
        st.image('arley.png')
        stc.html('''<p style="text-align: center;"><span style='font-family: "Comic Sans MS", sans-serif;'>ARLEY TORRES</span></p>
                <p style="text-align: center;"><span style='font-family: "Comic Sans MS", sans-serif;'>MATHEMATICS</span></p>''')
    
    with row2_2:
        st.image('sebs.png')
        stc.html('''<p style="text-align: center;"><span style='font-family: "Comic Sans MS", sans-serif;'>SEBASTIAN HURTADO</span></p>
                <p style="text-align: center;"><span style='font-family: "Comic Sans MS", sans-serif;'>INDUSTRIAL ENGINEER</span></p>''')
    with row2_3:
        st.image('sebas.png')
        stc.html('''<p style="text-align: center;"><span style='font-family: "Comic Sans MS", sans-serif;'>SEBASTIAN ESPINOSA</span></p>
                <p style="text-align: center;"><span style='font-family: "Comic Sans MS", sans-serif;'></span></p>''')
    
    with row3_1:
        st.image('\Photos and Logos\jose.png')
        stc.html('''<p style="text-align: center;"><span style='font-family: "Comic Sans MS", sans-serif;'>JOSE LUIS GOMEZ</span></p>
                <p style="text-align: center;"><span style='font-family: "Comic Sans MS", sans-serif;'>PETROLEUM ENGINEER</span></p>''')
        
    
    with row3_2:
        st.image('manuel.png')
        stc.html('''<p style="text-align: center;"><span style='font-family: "Comic Sans MS", sans-serif;'>MANUEL FIGUEREDO</span></p>
                <p style="text-align: center;"><span style='font-family: "Comic Sans MS", sans-serif;'></span></p>''')
    
    with row3_3:
        st.image('simon.png')
        stc.html('''<p style="text-align: center;"><span style='font-family: "Comic Sans MS", sans-serif;'>SIMON GALEANO</span></p>
                <p style="text-align: center;"><span style='font-family: "Comic Sans MS", sans-serif;'>STATISTICIAN</span></p>''')
    