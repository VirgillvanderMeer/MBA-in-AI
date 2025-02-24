import streamlit as st

st.title("De Juridische Briefhulp ⚖️✍️📜")
st.write("Genereer eenvoudig de Beslissing op bezwaar. ✅🔄🤝🚀")

naam = st.text_area("Typ of plak hier het Bezwaarschrift", height=300)

if st.button("Klik hier"):
    st.success("Je hebt op de knop geklikt!")

# Sidebar (left)
with st.sidebar:
    st.header("🔍 Invoer gegevens")

# Invoervelden in de sidebar
voorletters = st.sidebar.text_input("Voorletter(s) + achternaam")
straatnaam = st.sidebar.text_input("Straatnaam + huisnummer")
postcode = st.sidebar.text_input("Postcode + plaats")

# Opslaan-knop in de sidebar
if st.sidebar.button("Opslaan"):
    st.success(f"✅ Opgeslagen gegevens:\n\n"
               f"**Naam**: {voorletters} {achternaam}\n"
               f"**Adres**: {straatnaam} {huisnummer}\n"
               f"**Postcode en Plaats**: {postcode} {plaats}")

    # Dropdown-keuze
    keuze = st.selectbox("📌 Kies een categorie:", ["Optie A", "Optie B", "Optie C"])

    # Checkbox
    akkoord = st.checkbox("✅ Ga akkoord met de voorwaarden")

    # Schuifregelaar
    leeftijd = st.slider("🎂 Kies je leeftijd", 18, 100, 25)

    # Knop
    submit = st.button("🚀 Verstuur")

