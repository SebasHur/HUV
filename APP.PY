import streamlit as st
from PIL import Image
#El boton destremlit debe ser lo primero
img = Image.open('data/logo2.png')
#Method 1
st.set_page_config(page_title='Hospital Universitario',
         page_icon = img, layout='wide',
       initial_sidebar_state='collapsed')






def main():
    """All code goes here""" 
    st.title('Hello Streamlit Lovers')
    st.sidebar.success('Menu')

if __name__ == '__main__':
    main()
