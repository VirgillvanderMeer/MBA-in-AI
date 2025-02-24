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
        div[data-testid="stTextInput"] {
            margin-bottom: -40px !important; /* Verklein de ruimte tussen invoervelden */
        }
        
        /* Verwijder ongewenste extra witruimte */
        section[data-testid="stSidebar"] div {
            padding-bottom: 0px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Invoervelden in de sidebar zonder labels, alleen placeholders
voorletters = st.sidebar.text_input("", placeholder="Voorletter(s) + achternaam")
straatnaam = st.sidebar.text_input("", placeholder="Straatnaam + huisnummer")
postcode = st.sidebar.text_input("", placeholder="Postcode + plaats")

# Opslaan-knop
if st.sidebar.button("Opslaan"):
    st.markdown(f"""
    ✅ **Opgeslagen gegevens:**  

{voorletters}  
{straatnaam}  
{postcode}  
    """)

    # Dropdown-keuze
    keuze = st.selectbox("📌 Kies een categorie:", ["Optie A", "Optie B", "Optie C"])

    # Checkbox
    akkoord = st.checkbox("✅ Ga akkoord met de voorwaarden")

    # Schuifregelaar
    leeftijd = st.slider("🎂 Kies je leeftijd", 18, 100, 25)

    # Knop
    submit = st.button("🚀 Verstuur")

