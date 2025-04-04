import streamlit as st
from PIL import Image
from Functions import get_eqn
from streamlit_paste_button import paste_image_button as pbutton
from bs4 import BeautifulSoup
import pathlib
import shutil

GA_ID = "google_analytics"
GA_SCRIPT = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-DJ7TKGY65Y"></script>
<script id='google_analytics'>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-DJ7TKGY65Y');
</script>
"""

def inject_ga():
    
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    soup = BeautifulSoup(index_path.read_text(), features="html.parser")
    if not soup.find(id=GA_ID): 
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            shutil.copy(bck_index, index_path)  
        else:
            shutil.copy(index_path, bck_index)  
        html = str(soup)
        new_html = html.replace('<head>', '<head>\n' + GA_SCRIPT)
        index_path.write_text(new_html)

inject_ga()



st.markdown("""
    <style>
    .centered-header {
        text-align: center;
        font-size: 600px;
        font-weight: bold;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

st.session_state.result="No equation detected"

st.markdown('<h1 class="centered-header">🔢 Equation Prompter 🔢</h1>', unsafe_allow_html=True)

st.markdown("""
    <style>
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    .fadeIn {
        animation: fadeIn 2s ease-out;
        color: black;  /* Set color to black */
        font-size: 200px;  /* Increase font size for a big title */
        font-weight: bold;  /* Optional: makes the text bold */
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="fadeIn">Transform your images into texts with just a button.</p>', unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)
# Create a paste button
paste_result = pbutton(
    label="📋 Click here to paste your image",
    text_color="#ffffff",
    background_color="#2fa4ed",
    hover_background_color="#1669f0",
)

with st.container(border=True):
    # If the image is uploaded, display it inside the box
    if paste_result.image_data is not None:
        st.image(paste_result.image_data, caption="Uploaded Image",use_container_width=True)
        st.session_state.result=get_eqn(paste_result.image_data)
    else:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.markdown('<h5 style="text-align: center;">Upload Image Here</h5>', unsafe_allow_html=True)
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")

st.write()
st.markdown(
    """
    <p style="font-size:20px;font-weight: bold">Equation in the image</p>
    """,
    unsafe_allow_html=True
)
with st.container(border=True):
    st.session_state.result=st.session_state.result.replace("\n","\n\n")
    st.markdown(st.session_state.result,unsafe_allow_html=True) 
    print(st.session_state.result)




