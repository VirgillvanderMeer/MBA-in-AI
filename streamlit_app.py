import streamlit as st

st.title("De Juridische Briefhulp ⚖️✍️📜")
st.write("Genereer eenvoudig de Beslissing op bezwaar. ✅🔄🤝🚀")

naam = st.text_input("Typ of plak hier het Bezwaarschrift")
if naam:
    st.write(f"Hallo, {naam}! 🎉")

if st.button("Klik hier"):
    st.success("Je hebt op de knop geklikt!")

# Sidebar (left)
with st.sidebar:
    st.header("🔍 Invoer gegevens")
    
    # Tekstinvoer
    naam = st.text_input("👤 Voorletters + Achternaam")

    # Dropdown-keuze
    keuze = st.selectbox("📌 Kies een categorie:", ["Optie A", "Optie B", "Optie C"])

    # Checkbox
    akkoord = st.checkbox("✅ Ga akkoord met de voorwaarden")

    # Schuifregelaar
    leeftijd = st.slider("🎂 Kies je leeftijd", 18, 100, 25)

    # Knop
    submit = st.button("🚀 Verstuur")

# Resultaten weergeven als gebruiker op de knop klikt
if submit:
    st.success(f"Hallo {naam}, je hebt {keuze} gekozen en bent {leeftijd} jaar oud.")
    if akkoord:
        st.info("Bedankt voor het akkoord gaan met de voorwaarden!")
    else:
        st.warning("Je moet akkoord gaan met de voorwaarden.")


