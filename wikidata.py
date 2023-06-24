import requests

# API endpoint URL
api_url = "https://en.wikipedia.org/w/api.php"

# Parameters for API request
params = {
    "action": "query",
    "format": "json",
    "prop": "extracts|pageimages",
    "exintro": True,
    "explaintext": True,
    "piprop": "original",
    "titles": "Músculo_glúteo_menor"
}

# Make the API request
response = requests.get(api_url, params=params)
data = response.json()

# Get the page content
pages = data["query"]["pages"]
page_id = next(iter(pages))
page_data = pages[page_id]

# Extract the image URL, muscle data, and other details
image_url = page_data.get("original", {}).get("source")
muscle_data = page_data.get("extract", "")
#irrigation = muscle_data.split("Irrigación")[1].split("Inervación")[0].strip()
#innervation = muscle_data.split("Inervacion")[1].split("Inserción")[0].strip()
#insertion = muscle_data.split("Inserción")[1].split("Origen")[0].strip()
#origin = muscle_data.split("Origen e inserción")[1].strip()

# Print the image URL and muscle details
print("Image URL:", image_url)
#print("Irrigation:", irrigation)
#print("Innervation:", innervation)
#print("Insertion:", insertion)
#print("Origin:", origin)
print(muscle_data)
