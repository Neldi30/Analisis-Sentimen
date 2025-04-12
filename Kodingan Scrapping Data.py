# 1. Install library
!pip install google-play-scraper pandas

# 2. Import library
from google_play_scraper import reviews, Sort
import pandas as pd

# 3. Scraping komentar Clash of Clans
app_id = 'com.supercell.clashofclans'

all_reviews = []
next_token = None

while len(all_reviews) < 3000:
    result, next_token = reviews(
        app_id,
        lang='id',         # Bahasa Indonesia
        country='id',      # Negara Indonesia
        sort=Sort.NEWEST,
        count=200,
        continuation_token=next_token
    )
    
    all_reviews.extend(result)
    print(f"Total komentar terkumpul: {len(all_reviews)}")

    if not next_token:
        break

# Potong ke 3000 jika lebih
all_reviews = all_reviews[:3000]

# 4. Proses dan beri label komentar // Disini saya atur sendiri menurut saya
data = []
for review in all_reviews:
    score = review['score']
    label = 'positif' if score >= 3 else 'negatif'
    data.append({
        'content': review['content'],
        'score': score,
        'label': label
    })

df = pd.DataFrame(data)

# 5. Simpan ke CSV
df.to_csv('Dataset Scraping Komentar Clash Of Clans.csv', index=False)
print(" Selesai! Data 3000 komentar disimpan.")

# 6. Download otomatis
from google.colab import files
files.download('Dataset Scraping Komentar Clash Of Clans.csv')
