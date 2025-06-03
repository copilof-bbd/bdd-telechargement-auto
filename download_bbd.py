import requests
import datetime

url = "https://www.data.gouv.fr/fr/datasets/r/a30ee196-26a7-40be-a152-f9f8fd6b7f72"
date_str = datetime.date.today().isoformat()
filename = f"fichier_{date_str}.csv"

# Télécharger le fichier et l’écraser s’il existe déjà
response = requests.get(url)
with open(filename, "wb") as f:
    f.write(response.content)

# Forcer un changement dans le dépôt pour déclencher un commit
with open("git_keepalive.txt", "w") as f:
    f.write(f"Téléchargement du fichier effectué le {date_str}")

print(f"✅ Fichier téléchargé : {filename}")

