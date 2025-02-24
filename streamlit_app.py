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

    # Keuzemenu
keuze = st.selectbox(
    "Welke gegevens wil je invoeren?",
    ["Voorletter(s) + Achternaam", "Straatnaam + Huisnummer", "Postcode + Plaats"]
)

# Toon de juiste invoervelden op basis van de keuze
if keuze == "Voorletter(s) + Achternaam":
    voorletters = st.text_input("Voorletter(s)")
    achternaam = st.text_input("Achternaam")
    if st.button("Opslaan"):
        st.success(f"Opgeslagen: {voorletters} {achternaam}")

elif keuze == "Straatnaam + Huisnummer":
    straatnaam = st.text_input("Straatnaam")
    huisnummer = st.text_input("Huisnummer")
    if st.button("Opslaan"):
        st.success(f"Opgeslagen: {straatnaam} {huisnummer}")

elif keuze == "Postcode + Plaats":
    postcode = st.text_input("Postcode")
    plaats = st.text_input("Plaats")
    if st.button("Opslaan"):
        st.success(f"Opgeslagen: {postcode} {plaats}")
    
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


