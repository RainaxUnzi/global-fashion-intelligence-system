import requests
import datetime
from bs4 import BeautifulSoup

# ---- API KEYS ----
GUARDIAN_API_KEY = "5d90d64d-c477-48e1-bea2-613576b85835"  # <-- paste your key here
NYT_API_KEY ="yJ5AYCGPrwthEphUFGhX302fEAAPFcyjdXQ4czGAAxTm2AAD"
import requests

# ──────────────────────────────────────────
# SOURCE 1: The Guardian
# ──────────────────────────────────────────
def scrape_guardian():
    """Fetches fashion articles from The Guardian API"""

    url = "https://content.guardianapis.com/search"
    params = {
        "section": "fashion",
        "api-key": GUARDIAN_API_KEY,
        "page-size": 20,
        "order-by": "newest",
    }

    articles = []

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        results = response.json()["response"]["results"]

        for item in results:
            articles.append({
                "title": item["webTitle"],
                "link": item["webUrl"],
                "source": "The Guardian",
                "scraped_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            })

        print(f"[Guardian] ✅ Fetched {len(articles)} articles")

    except Exception as e:
        print(f"[Guardian] ❌ Error: {e}")

    return articles


# ──────────────────────────────────────────
# SOURCE 2: New York Times
# ──────────────────────────────────────────
def scrape_nyt():
    """Fetches fashion articles from NYT Top Stories API"""

    url = f"https://api.nytimes.com/svc/topstories/v2/fashion.json"
    params = {
        "api-key": NYT_API_KEY
    }

    articles = []

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        results = response.json().get("results", [])

        for item in results:
            # Skip items with no title or link
            if not item.get("title") or not item.get("url"):
                continue

            articles.append({
                "title": item["title"],
                "link": item["url"],
                "source": "NYT Fashion",
                "scraped_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            })

        print(f"[NYT] ✅ Fetched {len(articles)} articles")

    except Exception as e:
        print(f"[NYT] ❌ Error: {e}")

    return articles
def scrape_vogue():
    """Fetches fashion articles from Vogue RSS feed"""

    url = "https://www.vogue.com/feed/rss"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    articles = []

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "xml")
        items = soup.find_all("item")

        for item in items:
            title = item.find("title")
            link = item.find("link")

            if not title or not link:
                continue

            articles.append({
                "title": title.get_text(strip=True),
                "link": link.get_text(strip=True),
                "source": "Vogue",
                "scraped_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            })

        print(f"[Vogue] ✅ Fetched {len(articles)} articles")

    except Exception as e:
        print(f"[Vogue] ❌ Error: {e}")

    return articles

def fetch_trend_images(unsplash_key):
    """Fetches fashion trend images from Paris, Milan, New York"""

    cities = [
        {"city": "Paris", "query": "paris fashion week runway 2026"},
        {"city": "Milan", "query": "milan fashion week runway 2026"},
        {"city": "New York", "query": "new york fashion week runway 2026"},
        {"city": "Global", "query": "fashion trends style 2026"},
    ]

    all_images = []

    for item in cities:
        url = "https://api.unsplash.com/search/photos"
        params = {
            "query": item["query"],
            "per_page": 4,
            "orientation": "portrait",
            "client_id": unsplash_key
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            results = response.json().get("results", [])

            for photo in results:
                all_images.append({
                    "city": item["city"],
                    "image_url": photo["urls"]["regular"],
                    "thumb_url": photo["urls"]["small"],
                    "photographer": photo["user"]["name"],
                    "unsplash_link": photo["links"]["html"],
                    "description": photo.get("alt_description", "Fashion trend")
                })

            print(f"[Unsplash] ✅ {item['city']} — {len(results)} images fetched")

        except Exception as e:
            print(f"[Unsplash] ❌ {item['city']} error: {e}")

    return all_images
# ──────────────────────────────────────────
# COMBINED: Run both scrapers together
# ──────────────────────────────────────────
UNSPLASH_KEY = "sIh9XVTLOTFyYe_lWrkJnthqM4cyUlbZ_ynIQA0Ws6s"  # <-- paste your key here

def scrape_all():
    """Runs all scrapers and returns combined results"""
    all_articles = []
    all_articles.extend(scrape_guardian())
    all_articles.extend(scrape_nyt())
    all_articles.extend(scrape_vogue())
    print(f"\n📦 Total articles collected: {len(all_articles)}")

    print("\n🖼 Fetching trend images...")
    images = fetch_trend_images(UNSPLASH_KEY)
    print(f"🖼 Total images fetched: {len(images)}")

    return all_articles, images

# Test
if __name__ == "__main__":
    results = scrape_all()
    print("\n--- SAMPLE (first 5) ---")
    for i, article in enumerate(results[:5], 1):
        print(f"\n{i}. [{article['source']}] {article['title']}")
        print(f"   {article['link']}")