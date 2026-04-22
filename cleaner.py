import pandas as pd

def clean_articles(articles):
    """Removes duplicates and junk from scraped articles"""

    # Convert list to DataFrame — makes cleaning much easier
    df = pd.DataFrame(articles)

    before = len(df)

    # 1. Remove duplicate links (same article from two sources)
    df = df.drop_duplicates(subset=["link"])

    # 2. Remove duplicate titles
    df = df.drop_duplicates(subset=["title"])

    # 3. Remove rows where title is too short (junk/ads)
    df = df[df["title"].str.len() > 20]

    # 4. Strip extra whitespace from titles
    df["title"] = df["title"].str.strip()

    after = len(df)

    print(f"[Cleaner] ✅ Cleaned: {before} → {after} articles ({before - after} removed)")

    return df