import pandas as pd
import os
import json

CSV_PATH = "data/articles.csv"
IMAGES_PATH = "data/trend_images.json"

def save_to_csv(df):
    """Saves articles to CSV, appending new ones only"""

    if os.path.exists(CSV_PATH):
        existing = pd.read_csv(CSV_PATH)
        combined = pd.concat([existing, df], ignore_index=True)
        combined = combined.drop_duplicates(subset=["link"])
        combined.to_csv(CSV_PATH, index=False)
        print(f"[Storage] ✅ CSV updated — {len(combined)} total articles saved")
    else:
        df.to_csv(CSV_PATH, index=False)
        print(f"[Storage] ✅ CSV created — {len(df)} articles saved")

def save_images(images):
    """Saves trend images to JSON file"""
    with open(IMAGES_PATH, "w") as f:
        json.dump(images, f, indent=2)
    print(f"[Storage] ✅ Images saved — {len(images)} trend images stored")