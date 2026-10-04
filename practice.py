import requests

path = "https://api.artic.edu/api/v1/artworks"

params = {
    "page" : 1,
    "limit" : 3,
}

response = requests.get(path, params=params)

if response.status_code == 200:
    data = response.json()

    for artwork in data["data"]:
        title = artwork.get("title")
        thumbnail = artwork.get("thumbnail")
        alt_text = thumbnail.get("alt_text") if thumbnail else None
        description = alt_text if alt_text else "No description available"

        print(title, description)

else:
    print(f"error : {response.status_code}")