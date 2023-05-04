import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello')
st.header('Welcome to Data :red[Science Internship] 2023')
st.subheader('Good Morning:sunglasses:')

st.write('##########################################')

# var = '''print('Hello World')'''
# st.code(var ,language='python')

# st.write('##########################################')

# df = pd.DataFrame(
#    np.random.randn(50, 20),
# columns=('col %d' % i for i in range(20)))

# st.dataframe(df)

# st.write('##########################################')

btn_click = st.button('Click kar be ith!')

if btn_click == True:
    st.subheader('Match Lavachi ka aaj?:sunglasses:')
    st.balloons()

st.write('##########################################')
st.snow()