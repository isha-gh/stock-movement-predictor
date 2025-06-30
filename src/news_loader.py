import subprocess
import os

DATA_DIR = 'data/raw'
DATA_FILE = 'top-25-world-news-2018-2023.csv'
DATA_PATH = os.path.join(DATA_DIR, DATA_FILE)

def download_kaggle_dataset():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_PATH):
        print("Downloading dataset from Kaggle...")
        subprocess.run([
            "kaggle", "datasets", "download",
            "suruchiarora/top-25-world-news-2018-2023",
            "--unzip",
            "-p", DATA_DIR
        ], check=True)
        print("Download complete.")
    else:
        print(f"Dataset already exists at {DATA_PATH}. Skipping download.")

if __name__ == "__main__":
    download_kaggle_dataset()

