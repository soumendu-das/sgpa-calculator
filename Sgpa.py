# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 21:01:29 2024

@author: Soumendu
"""
import streamlit as st
st.title("SGPA CALCULATOR")
coa=st.slider("Computer Architecture:- ",min_value =0,max_value=10)
de=st.slider("Digital Electronics:- ",min_value =0,max_value=10)
toc=st.slider("Automata Theory:- ",min_value =0,max_value=10)
math=st.slider("math:- ",min_value =0,max_value=10)
phy=st.slider("physics:- ",min_value =0,max_value=10)
coalab=st.slider("Computer Architecture lab:- ",min_value =0,max_value=10)
delab=st.slider("Digital Electronics lab:- ",min_value =0,max_value=10)
phylab=st.slider("physics lab:- ",min_value =0,max_value=10)
hu=st.slider("soft skill and apptitude:- ",min_value =0,max_value=10)
py=st.slider("python lab:- ",min_value =0,max_value=10)


if st.button("calculate sgpa"):
    ans=(coa*3)+(de*3)+(toc*3)+(math*2)+(phy*2)+(coalab*1.5)+(delab*1.5)+(phylab*1.5)+(py*1.5)+(hu*1)
    st.text(ans/20)