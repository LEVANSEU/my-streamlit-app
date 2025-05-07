
import streamlit as st
import pandas as pd

st.title("💼 Excel Generator App")

uploaded_report = st.file_uploader("Upload report.xlsx", type="xlsx")
uploaded_statement = st.file_uploader("Upload statement.xlsx", type="xlsx")

if uploaded_report and uploaded_statement:
    st.success("✅ Files uploaded!")
    purchases_df = pd.read_excel(uploaded_report, sheet_name='Grid')
    bank_df = pd.read_excel(uploaded_statement)

    st.write("### Report Preview", purchases_df.head())
    st.write("### Statement Preview", bank_df.head())

    if st.button("Generate Final File"):
        st.write("🚀 Generating... (this is a placeholder, real logic goes here)")
        st.success("✅ Final file generated!")
else:
    st.info("Please upload both Excel files.")
