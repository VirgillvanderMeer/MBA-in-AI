import streamlit as st

st.title("De juridische briefassistent App")
st.write("Genereer eenvoudig je beslissing op bezwaar.")

naam = st.text_input("Wat is je naam?")
if naam:
    st.write(f"Hallo, {naam}! 🎉")

if st.button("Klik hier"):
    st.success("Je hebt op de knop geklikt!")
