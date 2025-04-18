import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Folder buat simpan data
FOLDER_FLOORPLAN = 'data/FloorPlans'
FOLDER_METADATA = 'metadata'

# Bikin folder kalau belum ada
os.makedirs(FOLDER_FLOORPLAN, exist_ok=True)
os.makedirs(FOLDER_METADATA, exist_ok=True)

# List contoh URL gambar floorplan (sementara manual dulu ya)
floorplan_urls = [
    "https://photos.zillowstatic.com/fp/432c76f6f533605b917a5885f602aad9-sc_1920_1280.webp",
    "https://photos.zillowstatic.com/fp/2af92ea544eb1b6810f17ecf26e14af4-sc_1920_1280.webp",
    "https://photos.zillowstatic.com/fp/d9227389a847e68813a5a6ca762a4b2c-sc_1920_1280.webp",
    "https://photos.zillowstatic.com/fp/687edfa8ebd1dd557080b020de44b22c-sc_1920_1280.webp",
    "https://photos.zillowstatic.com/fp/d01a11425254bad1ba3a2dbd05bf2ec6-sc_1920_1280.webp",
]

# Data untuk metadata
metadata = []

# Mulai download satu-satu
for idx, url in enumerate(floorplan_urls):
    filename = f"floorplan_{idx+1}.jpg"
    filepath = os.path.join(FOLDER_FLOORPLAN, filename)

    print(f"Downloading {filename}...")

    # Download gambar
    response = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(response.content)

    # Simpan info metadata
    metadata.append({
        "file_name": filename,
        "project_type": "Residential",  # contoh sementara
        "region": "Global",             # contoh sementara
        "format": "JPG",
        "source_url": url
    })

# Save metadata ke CSV
metadata_df = pd.DataFrame(metadata)
metadata_csv_path = os.path.join(FOLDER_METADATA, "floorplan_metadata.csv")
metadata_df.to_csv(metadata_csv_path, index=False)

print("Download selesai dan metadata disimpan.")