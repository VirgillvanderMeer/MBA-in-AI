import streamlit as st
import re

st.title("De Juridische Briefhulp ⚖️✍️📜")
st.write("Genereer eenvoudig de Beslissing op bezwaar. ✅🔄🤝🚀")

naam = st.text_area("Typ of plak hier het Bezwaarschrift", height=300)

# Sidebar (left)
with st.sidebar:
    st.header("🔍 Invoer gegevens")

# CSS om de tussenruimte volledig te verkleinen
st.sidebar.markdown("""
    <style>
        /* Algemene dropdown styling */
        div[data-baseweb="select"] > div {
            background-color: #00274D !important; /* Donkerblauw achtergrond */
            color: white !important; /* Witte tekst */
            border-radius: 5px; /* Afgeronde hoeken */
        }

        /* Stijl de tekst van de dropdown opties */
        div[data-baseweb="popover"] {
            background-color: #00274D !important; /* Donkerblauw */
            color: white !important;
            border-radius: 5px;
        }

        /* Stijl de geselecteerde optie */
        div[data-baseweb="select"] span {
            color: white !important;
        }

        /* Stijl de hover-kleur van opties */
        div[data-baseweb="option"]:hover {
            background-color: #00509E !important; /* Iets lichtere blauw */
        }

        /* Stijl de rand van de dropdown */
        div[data-testid="stSelectbox"] {
            border: 1px solid white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Dropdown-keuze
keuze = st.sidebar.selectbox("", ["Natuurlijk persoon 👤", "Rechtspersoon 💼"])

st.write(f"Je hebt gekozen voor: **{keuze}**")

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

# Extra witruimte na het laatste invoerveld om de knop verder naar beneden te plaatsen
st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)

if st.sidebar.button("Opslaan"):
    output = "✅ **Opgeslagen gegevens:**\n"
    if keuze == "Rechtspersoon 💼" and onderneming.strip():
        output += f"Naam onderneming: {onderneming}\n"
    else:
        output += "Natuurlijk persoon\n"
    output += f"Zaaknummer: {zaaknummer}\n"
    st.markdown(output)

def is_valid_zaaknummer(zaaknummer):
    pattern = r"^(JB|WO)\.(1[8-9]|2[0-9]|30)\.\d{6}\.\d{3}$"
    return bool(re.match(pattern, zaaknummer))

if st.button("Klik hier"):
    if not naam.strip():
        st.warning("Vul eerst het bezwaarschrift in voordat je verder gaat.")
    elif not is_valid_zaaknummer(zaaknummer):
        st.warning("Vul een geldig zaaknummer in volgens het patroon JB.25.123456.001 of WO.25.123456.001")
    else:
        st.success("Je Bob zit in de oven...🧑‍🍳🔥🔥...en is bijna klaar! 🍩🍰🍕")

    # Checkbox
    akkoord = st.checkbox("✅ Ga akkoord met de voorwaarden")

    # Schuifregelaar
    leeftijd = st.slider("🎂 Kies je leeftijd", 18, 100, 25)

    # Knop
    submit = st.button("🚀 Verstuur")

