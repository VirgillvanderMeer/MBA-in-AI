import streamlit as st

st.title("De Juridische Briefhulp ⚖️✍️📜")
st.write("Genereer eenvoudig de Beslissing op bezwaar. ✅🔄🤝🚀")

naam = st.text_area("Typ of plak hier het Bezwaarschrift", height=300)

if st.button("Klik hier"):
    st.success("Je Bob zit in de oven...🧑‍🍳🔥🔥...en is bijna klaar! 🍩🍰🍕")

# Sidebar (left)
with st.sidebar:
    st.header("🔍 Invoer gegevens")

# Invoervelden in de sidebar met standaardtekst
voorletters = st.sidebar.text_input("Voorletter(s) + Achternaam", value="J. de Vries")
straatnaam = st.sidebar.text_input("Straatnaam + Huisnummer", value="Hoofdstraat 12")
postcode = st.sidebar.text_input("Postcode + Plaats", value="1234 AB, Amsterdam")

# Opslaan-knop
if st.sidebar.button("Opslaan"):
    st.success(f"✅ Opgeslagen gegevens:\n\n"
               f"****: {voorletters}\n"
               f"****: {straatnaam}\n"
               f"****: {postcode}")

    # Dropdown-keuze
    keuze = st.selectbox("📌 Kies een categorie:", ["Optie A", "Optie B", "Optie C"])

    # Checkbox
    akkoord = st.checkbox("✅ Ga akkoord met de voorwaarden")

    # Schuifregelaar
    leeftijd = st.slider("🎂 Kies je leeftijd", 18, 100, 25)

    # Knop
    submit = st.button("🚀 Verstuur")

