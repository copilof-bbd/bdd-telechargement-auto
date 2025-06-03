import requests
import datetime
import os

# Créer le dossier "data" s'il n'existe pas
os.makedirs("data", exist_ok=True)

# Définir l’URL et le nom du fichier
url = "https://www.data.gouv.fr/fr/datasets/r/a30ee196-26a7-40be-a152-f9f8fd6b7f72"
date_str = datetime.date.today().isoformat()
filename = f"data/fichier_{date_str}.csv"

# Télécharger et sauvegarder
response = requests.get(url)
with open(filename, "wb") as f:
    f.write(response.content)

print(f"✅ Fichier téléchargé : {filename}")
