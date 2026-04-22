import json

def load_keywords():
    """Loads keywords from keywords.json"""
    with open("keywords.json", "r") as f:
        return json.load(f)

def scan_articles(df):
    """Scans all articles for keyword matches"""
    keywords = load_keywords()
    alerts = []

    for _, row in df.iterrows():
        title_lower = row["title"].lower()
        matched_keywords = []
        matched_category = []

        for category, words in keywords.items():
            for word in words:
                if word.lower() in title_lower:
                    matched_keywords.append(word)
                    matched_category.append(category)

        if matched_keywords:
            alerts.append({
                "title": row["title"],
                "link": row["link"],
                "source": row["source"],
                "scraped_at": row["scraped_at"],
                "matched_keywords": list(set(matched_keywords)),
                "categories": list(set(matched_category))
            })

    print(f"[Alerts] ✅ Found {len(alerts)} matching articles")
    return alerts


def save_alerts(alerts):
    """Saves alerts to JSON file for the dashboard"""
    with open("data/alerts.json", "w") as f:
        json.dump(alerts, f, indent=2)
    print(f"[Alerts] ✅ Saved {len(alerts)} alerts to data/alerts.json")