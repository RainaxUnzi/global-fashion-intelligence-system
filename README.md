# Fashion Intel 
### Global Fashion Intelligence System

> An automated Python system that scrapes fashion articles from The Guardian, NYT, and Vogue — cleans the data, detects trends, and delivers a daily HTML email digest with a live web dashboard.

---

##  Live Dashboard Preview

The dashboard displays global fashion trends across Paris, Milan, New York, and more — with real-time article feeds from 3 major sources.

---

##  Features

- **Multi-source scraping** — pulls articles from The Guardian API, NYT Top Stories API, and Vogue RSS feed
- **Smart data cleaning** — removes duplicates, junk titles, and ads automatically
- **Keyword-based trend alerts** — scans articles against a configurable `keywords.json` for category-tagged alerts
- **CSV storage** — appends new articles daily without duplicates
- **HTML email digest** — sends a beautifully styled daily summary via Gmail SMTP
- **Live dashboard** — editorial-style web UI showing articles by source and trend images by fashion capital
- **Daily automation** — runs automatically every day at 08:00 AM using `schedule`

---

##  Project Structure

```
fashion-intel/
│
├── main.py              # Entry point — orchestrates the full pipeline
├── scraper.py           # Fetches articles from Guardian, NYT, Vogue + Unsplash images
├── cleaner.py           # Cleans and deduplicates raw article data
├── storage.py           # Saves articles to CSV and images to JSON
├── alerts.py            # Keyword scanning and trend alert generation
├── emailer.py           # Builds and sends HTML email digest via Gmail SMTP
├── dashboard.html       # Frontend dashboard (editorial newspaper style)
├── keywords.json        # Configurable keyword categories for trend detection
│
└── data/
    ├── articles.csv     # Stored articles (auto-updated daily)
    ├── alerts.json      # Latest trend alerts
    └── trend_images.json # Fashion capital images from Unsplash
```

---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| `requests` | HTTP calls to APIs and RSS feeds |
| `BeautifulSoup` | XML parsing for Vogue RSS |
| `pandas` | Data cleaning and CSV management |
| `smtplib` | Email delivery via Gmail SMTP |
| `schedule` | Daily automation at 08:00 AM |
| Guardian API | Fashion section articles |
| NYT Top Stories API | Fashion section articles |
| Vogue RSS | Latest Vogue articles |
| Unsplash API | Trend images by fashion capital |

---

##  Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/fashion-intel.git
cd fashion-intel
```

### 2. Install dependencies
```bash
pip install requests beautifulsoup4 pandas schedule lxml
```

### 3. Add your API keys

Open `scraper.py` and fill in:
```python
GUARDIAN_API_KEY = "your_guardian_key"
NYT_API_KEY      = "your_nyt_key"
UNSPLASH_KEY     = "your_unsplash_key"
```

Open `emailer.py` and fill in:
```python
SENDER_EMAIL    = "your_gmail@gmail.com"
SENDER_PASSWORD = "your_app_password"   # Gmail App Password, NOT your login password
RECEIVER_EMAIL  = "recipient@gmail.com"
```

> **Getting a Gmail App Password:** Go to [myaccount.google.com](https://myaccount.google.com) → Search "App Passwords" → Generate one for Mail.

### 4. Run the system
```bash
python main.py
```

### 5. View the dashboard
```bash
# In a second terminal, from the fashion-intel folder:
python -m http.server 8000 --bind 127.0.0.1
```
Then open `dashboard.html` in your browser.

---

##  API Keys Required

| API | Free Tier | Get Key |
|-----|-----------|---------|
| The Guardian | ✅ Free | [open-platform.theguardian.com](https://open-platform.theguardian.com) |
| New York Times | ✅ Free | [developer.nytimes.com](https://developer.nytimes.com) |
| Unsplash | ✅ Free | [unsplash.com/developers](https://unsplash.com/developers) |

---

##  Email Digest Sample

The daily email includes:
- **Trend Alerts** — articles matching your configured keywords, tagged by category
- **Top Articles** — top 3 articles per source (Guardian, NYT, Vogue)
- Styled HTML layout with Fashion Intel branding

---

##  How It Works

```
main.py runs the full pipeline:

1. scraper.py   →  Fetches articles from 3 sources + Unsplash images
2. cleaner.py   →  Removes duplicates, short titles, whitespace junk
3. storage.py   →  Saves to data/articles.csv and data/trend_images.json
4. alerts.py    →  Scans titles against keywords.json → saves data/alerts.json
5. emailer.py   →  Builds HTML email and delivers via Gmail SMTP
6. schedule     →  Repeats daily at 08:00 AM automatically
```

---

##  Keywords Configuration

Edit `keywords.json` to customise what trends get flagged:

```json
{
  "Sustainability": ["sustainable", "eco", "recycled", "upcycled"],
  "Luxury": ["Chanel", "Dior", "Gucci", "Prada", "Hermès"],
  "Trends": ["runway", "fashion week", "collection", "spring", "autumn"]
}
```

---

##  Future Improvements

- [ ] Selenium scraping for JavaScript-heavy sites
- [ ] Trend frequency charts over time
- [ ] Keyword alert frequency heatmap
- [ ] Telegram / WhatsApp notification support
- [ ] Hosted dashboard (Netlify / GitHub Pages)

---

##  Author

Built by **Raina Mansoor** as a personal portfolio project (2026).  
A practical demonstration of Python automation, API integration, data cleaning, and frontend development.

---

##  License

MIT License — free to use and modify.
