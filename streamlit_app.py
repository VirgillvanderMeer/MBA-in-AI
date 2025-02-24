import streamlit as st

st.title("De Juridische Briefhulp ⚖️✍️📜")
st.write("Genereer eenvoudig de Beslissing op bezwaar. ✅🔄🤝🚀")

naam = st.text_area("Typ of plak hier het Bezwaarschrift", height=300)

if st.button("Klik hier"):
    st.success("Je Bob zit in de oven...🧑‍🍳🔥🔥...en is bijna klaar! 🍩🍰🍕")

# Sidebar (left)
with st.sidebar:
    st.header("🔍 Invoer gegevens")

# Invoervelden in de sidebar zonder titels, alleen placeholders
voorletters = st.sidebar.text_input("", placeholder="Voorletter(s) + Achternaam")
straatnaam = st.sidebar.text_input("", placeholder="Straatnaam + Huisnummer")
postcode = st.sidebar.text_input("", placeholder="Postcode + Plaats")

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

