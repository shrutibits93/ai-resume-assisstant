import streamlit as st
import ResumeJD_Compare
from ResumeJD_Compare import enhance_text

st.title("Resume Enhancer.")

JD = st.text_area("Job Description")
Resume = st.text_area("Resume text")

if st.button("Run"):
    output = enhance_text(Resume, JD)
    st.text_area("Output", value=output, height=250)
