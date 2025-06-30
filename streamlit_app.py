import streamlit as st
import pandas as pd
from datetime import datetime
import os
#st.title("🎈 My new Streamlit app")
#st.write(
#    "Welcome"
#)


# -------------------------------
# Configuration
# -------------------------------
NOMS = ["Alice", "Bob", "Charlie", "Diane"]
FICHIER_HISTORIQUE = "historique.csv"

# -------------------------------
# Effacer l'historique si besoin
# Décommente cette ligne UNE FOIS pour réinitialiser :
if os.path.exists(FICHIER_HISTORIQUE): os.remove(FICHIER_HISTORIQUE)

# -------------------------------
# Charger l'historique s'il existe
# -------------------------------
if os.path.exists(FICHIER_HISTORIQUE):
    historique = pd.read_csv(FICHIER_HISTORIQUE)
else:
    historique = pd.DataFrame(columns=["Nom", "Valeur", "Date"])

# -------------------------------
# Titre de l'appli
# -------------------------------
st.title("Saisie de valeurs")

# -------------------------------
# Formulaire
# -------------------------------
with st.form("formulaire_saisie"):
    valeurs = {}
    for nom in NOMS:
        valeur = st.text_input(f"Valeur pour {nom}")
        valeurs[nom] = valeur

    bouton_submit = st.form_submit_button("Valider")

# -------------------------------
# Enregistrer les données
# -------------------------------
if bouton_submit:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nouvelles_lignes = []
    for nom, valeur in valeurs.items():
        nouvelles_lignes.append({"Nom": nom, "Valeur": valeur, "Date": timestamp})
    
    nouveau_df = pd.DataFrame(nouvelles_lignes, columns=["Nom", "Valeur", "Date"])
    historique = pd.concat([historique, nouveau_df], ignore_index=True)

    historique.to_csv(FICHIER_HISTORIQUE, index=False)

    st.success("✅ Saisie enregistrée !")

# -------------------------------
# Afficher l'historique
# -------------------------------
if not historique.empty:
    st.subheader("📊 Historique des saisies")
    st.dataframe(historique)
else:
    st.info("Aucune donnée enregistrée pour l'instant.")


