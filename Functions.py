
import google.generativeai as genai
import streamlit as st
#from apikeys import gemini_api_key

def get_eqn(image):
    genai.configure(api_key=st.secrets["gemini_api_key"])
    model=genai.GenerativeModel('gemini-1.5-pro')
    prompt="Rewrite the equation exactly as it is(dont write any descriptions) in standard mathematical notation and not in latex notation. And also use the _ symbol to represent subscripts instead of <sub> and </sub>, if there are no equations in the image just type No Equation Detected"
    response=model.generate_content([image,prompt])
    return(response.text)

