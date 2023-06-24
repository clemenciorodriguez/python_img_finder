import requests
from bs4 import BeautifulSoup

# URL del artículo de Wikipedia
url = "https://en.wikipedia.org/wiki/Gluteus_maximus_(muscle)"

# Realizar la solicitud HTTP
response = requests.get(url)

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(response.content, "html.parser")

# Encontrar el panel lateral infobox
infobox = soup.find("table", class_="infobox")

# Extraer la información deseada del panel lateral infobox
irrigation = ""
innervation = ""
insertion = ""
origin = ""

if infobox:
    rows = infobox.find_all("tr")
    for row in rows:
        header = row.find("th")
        if header:
            header_text = header.get_text().strip()
            if header_text == "Irrigation":
                irrigation = row.find("td").get_text().strip()
            elif header_text == "Innervation":
                innervation = row.find("td").get_text().strip()
            elif header_text == "Insertion":
                insertion = row.find("td").get_text().strip()
            elif header_text == "Origin":
                origin = row.find("td").get_text().strip()

# Imprimir la información extraída
print("Irrigation:", irrigation)
print("Innervation:", innervation)
print("Insertion:", insertion)
print("Origin:", origin)
