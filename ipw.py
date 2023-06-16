import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title= "العالمي" , layout= "wide")

def load_lottieurl(url):
 r = requests.get(url)
 if r.status_code != 200:
  return None
 return r.json()

lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_j2rjqphu.json")

with st.container():
 st.title("العالمي")
st.subheader("تمت برمجة الموقع من قبل عمر")
st.subheader("موقع يعرض شرح مستر اسلام") 

with st.container():
 st.write("---")
 left_column, right_column = st.columns(2)
 st.header("مازا افعل")
 st.write(
       """
       - تعلم النحو
       - اسمع الفصص
       - حفظ القرأن الكريم

       """
 )

 
with right_column:
 st_lottie(lottie_coding, height=300, key="coding")