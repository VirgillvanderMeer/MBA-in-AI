import streamlit as st

st.title("Mijn Streamlit App")
st.write("Dit is een testapp om te deployen via Streamlit Cloud.")

naam = st.text_input("Wat is je naam?")
if naam:
    st.write(f"Hallo, {naam}! 🎉")

if st.button("Klik hier"):
    st.success("Je hebt op de knop geklikt!")
