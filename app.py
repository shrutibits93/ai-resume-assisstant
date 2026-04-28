import streamlit as st
from ResumeJD_Compare import compare_resumes, enhance_text, dynamic_height

st.title("Resume Assistant")

JD = st.text_area("Job Description")
Resume = st.text_area("Resume text")

# Initialize session state
if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "tailored" not in st.session_state:
    st.session_state.tailored = False

if "skipped" not in st.session_state:
    st.session_state.skipped = False

if "analysis_output" not in st.session_state:
    st.session_state.analysis_output = ""

if "tailored_output" not in st.session_state:
    st.session_state.tailored_output = ""

# STEP 1: Submit
if st.button("Submit"):
    st.session_state.submitted = True
    st.session_state.analysis_output = compare_resumes(Resume, JD)

# STEP 2: Show analysis
if st.session_state.submitted:
    st.text_area("Match Analysis", value=st.session_state.analysis_output, height=dynamic_height(st.session_state.analysis_output))

    if st.button("Proceed with Tailoring"):
        st.session_state.tailored = True
        st.session_state.tailored_output = enhance_text(Resume, JD)

    if st.button("Skip Job"):
        st.session_state.skipped = True


# STEP 3: Show tailoring output
if st.session_state.tailored:
    st.text_area("Tailored Output", value=st.session_state.tailored_output, height=dynamic_height(st.session_state.tailored_output))

    # Rewrite
    if st.button("Rewrite Resume"):
        st.session_state.tailored_output = enhance_text(
            st.session_state.tailored_output, JD
        )

    # Download
    st.download_button(
        label="Download Resume",
        data=st.session_state.tailored_output,
        file_name="tailored_resume.txt"
    )

# OR Skip
if st.session_state.skipped:
    st.warning("Try another job description.")


