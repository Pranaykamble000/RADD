import streamlit as st
from utils import analyze_text 

st.set_page_config(page_title="RADD - Responsible AI Decision Dashboard", 
                   layout="centered")
                
st.title("RADD:Responsible AI Decision Dashboard")
st.write("Analyze text for sentiment,bias, and ethical risks.")

user_input = st.text_area("Enter text to analyze", height=200)

if st.button("Analyze"):
    if user_input.strip():
        result = analyze_text(user_input) 
        st.markdown(f"**Sentiment:** {result['sentiment']}")
        st.markdown(f"**Ethics Assessment:** {result['ethics']}")

        st.markdown(f"**Explanation:** {result['explanation']}")
    else:
        st.warning("Please enter some text.")