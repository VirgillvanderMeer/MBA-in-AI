import streamlit as st

st.title("De Juridische Briefhulp ⚖️✍️📜")
st.write("Genereer eenvoudig de Beslissing op bezwaar. ✅🔄🤝🚀")

naam = st.text_area("Typ of plak hier het Bezwaarschrift", height=300)

if st.button("Klik hier"):
    st.success("Je Bob zit in de oven...🧑‍🍳🔥🔥...en is bijna klaar! 🍩🍰🍕")

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

# Extra witruimte na het laatste invoerveld om de knop verder naar beneden te plaatsen
st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)

# Opslaan-knop
if st.sidebar.button("Opslaan"):
    # Postcode en plaats splitsen (ervan uitgaande dat er een spatie tussen zit)
    parts = postcode.split(" ", 1)
    postcode_clean = parts[0] if len(parts) > 0 else ""
    plaats = parts[1].upper() if len(parts) > 1 else ""  # Zet plaatsnaam in hoofdletters
    st.markdown(f"""
    ✅ **Opgeslagen gegevens:**  

    {voorletters}  
    {straatnaam}  
    {postcode_clean} {plaats}  
    """)

    # Dropdown-keuze
    keuze = st.selectbox("📌 Kies een categorie:", ["Optie A", "Optie B", "Optie C"])

    # Checkbox
    akkoord = st.checkbox("✅ Ga akkoord met de voorwaarden")

    # Schuifregelaar
    leeftijd = st.slider("🎂 Kies je leeftijd", 18, 100, 25)

    # Knop
    submit = st.button("🚀 Verstuur")

