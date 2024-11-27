import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Gavin Brumfield, M.S. in Analytics Candidate')

st.info('Inquisitive mind, fueled by a passion for uncovering patterns and making data-driven decisions. Leverages a diagnostic mindset and analytical rigor to navigate complex challenges, delivering actionable insights that enhance outcomes and drive strategic initiatives.')

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/gavinbrumfield/', 'Follow me on LinkedIn', icon_size)
