import schedule
import time
from scraper import scrape_all
from cleaner import clean_articles
from storage import save_to_csv, save_images
from alerts import scan_articles, save_alerts
from emailer import send_email


def generate_summary(df):
    summary = "=" * 50 + "\n"
    summary += "👗 GLOBAL FASHION INTELLIGENCE — DAILY DIGEST\n"
    summary += "=" * 50 + "\n\n"

    for source in df["source"].unique():
        source_df = df[df["source"] == source]
        summary += f"📰 {source} ({len(source_df)} articles)\n"
        summary += "-" * 40 + "\n"
        for i, row in enumerate(source_df.head(5).itertuples(), 1):
            summary += f"{i}. {row.title}\n"
            summary += f"   🔗 {row.link}\n\n"

    summary += "=" * 50 + "\n"
    summary += f"📦 Total articles today: {len(df)}\n"
    summary += "=" * 50 + "\n"
    return summary


def run():
    print("🚀 Starting Fashion Intel...\n")

    # Step 1: Scrape
    raw_articles, images = scrape_all()

    # Step 2: Clean
    clean_df = clean_articles(raw_articles)

    # Step 3: Save articles + images
    save_to_csv(clean_df)
    save_images(images)

    # Step 4: Scan for alerts
    alerts = scan_articles(clean_df)
    save_alerts(alerts)

    # Step 5: Send email
    send_email(alerts, clean_df)

    # Step 6: Print summary
    summary = generate_summary(clean_df)
    print("\n" + summary)

    print("✅ Done!\n")


if __name__ == "__main__":
    print("⏰ Scheduler started — will run daily at 08:00 AM")
    print("💡 Press Ctrl+C to stop\n")

    run()

    schedule.every().day.at("08:00").do(run)

    while True:
        schedule.run_pending()
        time.sleep(60)