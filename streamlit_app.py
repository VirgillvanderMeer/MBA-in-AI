import streamlit as st
import re
import datetime

st.title("LegalCheck - De Briefhulp ⚖️✍️📜")
st.write("Genereer eenvoudig de Beslissing op bezwaar. ✅🔄🤝🚀")

naam = st.text_area("Typ of plak hier het Bezwaarschrift", height=300)

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

# Lijst met datums genereren (bijvoorbeeld komende 30 dagen)
vandaag = datetime.date.today()
datums = [(vandaag + datetime.timedelta(days=i)) for i in range(31)]

# Maandnamen in Nederlands
maanden = {
    1: "januari", 2: "februari", 3: "maart", 4: "april", 5: "mei", 6: "juni",
    7: "juli", 8: "augustus", 9: "september", 10: "oktober", 11: "november", 12: "december"
}

# Lijst met uitgeschreven datums
uitgeschreven_datums = [f"{d.day} {maanden[d.month]} {d.year}" for d in datums]
boetedatum = st.sidebar.date_input("👮‍♀️📆 Kies de boetedatum", value=datetime.date.today())

# Standaarddatum instellen (vandaag in DD-MM-YYYY)
standaard_datum = datetime.date.today().strftime("%d-%m-%Y")

# Tekstinvoer voor datum
boetedatum = st.sidebar.text_input("👮‍♀️📆 Voer de boetedatum in (DD-MM-YYYY)", standaard_datum)

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

    # Knop
    submit = st.button("🚀 Verstuur")

