import streamlit as st
import re
import datetime
from PIL import Image
import requests

# Gebruikersinvoer voor voorletters en achternaam
voorletters = st.sidebar.text_input("", placeholder="Voorletter(s) + achternaam 👤")

# Verstuur data naar de Flask API
if st.button("🚀 Verstuur"):
    api_url = "http://127.0.0.1:5000/genereer_brief"
    response = requests.post(api_url, json={"voorletters": voorletters, "achternaam": achternaam})

    if response.status_code == 200:
        replacements = response.json()
        st.success(f"Briefgegevens gegenereerd: {replacements}")
    else:
        st.error("Er is iets misgegaan met de API.")


st.title("LegalCheck: De Briefhulp ⚖️✍️📜")
st.write("Genereer eenvoudig de Beslissing op bezwaar. 🔄🤝🚀")

verballisant = st.text_area("✅ Typ of plak hier de Waarneming van de verballisant", height=200)
bezwaarschrift = st.text_area("✅ Typ of plak hier het Bezwaarschrift", height=200)
hoorzitting = st.text_area("✅ Typ hier de besproken punten in de Telefonische hoorzitting", height=200)

# Sidebar (left)
with st.sidebar:
    st.header("🔍 Invoer gegevens")

# CSS om de tussenruimte volledig te verkleinen
st.sidebar.markdown("""
    <style>
        /* Verwijder de standaard marges tussen invoervelden */
        div[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div {
            margin-bottom: 0px;  /* Negatieve marge om velden dichter op elkaar te zetten */
            padding-bottom: 0px;
        }

        /* Verwijder extra padding in de invoervelden */
        div[data-testid="stSelectbox"] {
            margin-bottom: -40px !important; /* Verklein de ruimte tussen invoervelden */
        }
        
        /* Verwijder extra padding in de invoervelden */
        div[data-testid="stTextInput"] {
            margin-bottom: -40px !important; /* Verklein de ruimte tussen invoervelden */
        }
        
        /* Verwijder ongewenste extra witruimte */
        section[data-testid="stSidebar"] div {
            padding-bottom: 0px !important;
        }

    <style>
        .main {
            max-width: 2200px; /* Standaard is rond de 700px */
        }
    </style>
""", unsafe_allow_html=True)

# Dropdown-keuze
keuze = st.sidebar.selectbox("", ["Natuurlijk persoon 👤", "Rechtspersoon 💼"])

# Invoervelden in de sidebar zonder labels, alleen placeholders
if keuze == "Natuurlijk persoon 👤":
    voorletters = st.sidebar.text_input("", placeholder="Voorletter(s) + achternaam 👤")
    straatnaam = st.sidebar.text_input("", placeholder="Straatnaam + huisnummer 🏡")
    postcode = st.sidebar.text_input("", placeholder="Postcode + plaats 📬")
    
elif keuze == "Rechtspersoon 💼":
    onderneming = st.sidebar.text_input("", placeholder="Naam onderneming 💼")
    voorletters = st.sidebar.text_input("", placeholder="Voorletter(s) + achternaam 👤")
    straatnaam = st.sidebar.text_input("", placeholder="Straatnaam + huisnummer 🏡")
    postcode = st.sidebar.text_input("", placeholder="Postcode + plaats 📬")

zaaknummer = st.sidebar.text_input("", placeholder="Zaaknummer 📂 (JB.25.123456.001)")
jurist = st.sidebar.text_input("", placeholder="Naam jurist + e-mail 📧")
bijlage = st.sidebar.text_input("", value="Boetebesluit met instructies", placeholder="Bijlage(n) 📎")

# Extra witruimte toevoegen vóór de boetedatum
st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)

# Lijst met uitgeschreven datums
besluitdatum = st.sidebar.date_input("👮‍♀️📆 Kies de besluitdatum", value=datetime.date.today())

# Lijst met uitgeschreven datums
bezwaardatum = st.sidebar.date_input("✍️📆 Kies de bezwaardatum", value=datetime.date.today())

# Standaarddatum instellen (vandaag in DD-MM-YYYY)
standaard_datum = datetime.date.today().strftime("%d-%m-%Y")

# Extra witruimte na het laatste invoerveld om de knop verder naar beneden te plaatsen
st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)

if st.sidebar.button("Opslaan"):
    output = "✅ **Opgeslagen gegevens:**\n"
    if keuze == "Rechtspersoon 💼" and onderneming.strip():
        output += f"Naam onderneming: {onderneming}\n"
    else:
        output += "\n"
    output += f" {zaaknummer}\n"
    st.markdown(output)

def is_valid_zaaknummer(zaaknummer):
    pattern = r"^(JB|WO)\.(1[8-9]|2[0-9]|30)\.\d{6}\.\d{3}$"
    return bool(re.match(pattern, zaaknummer))

if st.button("🚀 Verstuur"):
    if not bezwaarschrift.strip():
        st.warning("Vul eerst het bezwaarschrift in voordat je verder gaat.")
    elif not is_valid_zaaknummer(zaaknummer):
        st.warning("Vul een geldig zaaknummer in volgens het patroon JB.25.123456.001 of WO.25.123456.001")
    else:
        st.success("Je Bob zit in de oven...🧑‍🍳🥖🔥🔥...en is bijna klaar! 🍩🍰🍕")
