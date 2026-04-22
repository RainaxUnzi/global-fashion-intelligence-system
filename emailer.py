import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ── Mailtrap credentials ──
MAILTRAP_HOST     = "live.smtp.mailtrap.io"
MAILTRAP_PORT     = 587
MAILTRAP_USERNAME = "api"
MAILTRAP_PASSWORD = "5a54494afba73ab59fde3f521ea3b99e"  # <-- paste the token you just copied

SENDER_EMAIL = "rainamansoor3@gmail.com"
RECEIVER_EMAIL = "rainamansoor3@gmail.com"    # <-- your real email


def build_email_body(alerts, articles_df):
    """Builds a nice HTML email with alerts and top articles"""

    # ── ALERTS SECTION ──
    alerts_html = ""
    if alerts:
        alerts_html = "<h2 style='color:#c8a96e;'>🔔 Trend Alerts</h2>"
        for alert in alerts[:10]:
            keywords = ", ".join(alert["matched_keywords"])
            categories = ", ".join(alert["categories"])
            alerts_html += f"""
            <div style='border-left:3px solid #c8a96e;padding:10px 16px;margin:12px 0;background:#fffdf7;'>
                <div style='font-size:12px;color:#8a8278;text-transform:uppercase;letter-spacing:1px;'>{categories} — {keywords}</div>
                <div style='font-size:16px;font-weight:bold;margin:6px 0;'>{alert['title']}</div>
                <a href='{alert['link']}' style='color:#c8a96e;font-size:13px;'>Read article →</a>
            </div>"""
    else:
        alerts_html = "<p style='color:#8a8278;'>No trend alerts today.</p>"

    # ── TOP ARTICLES SECTION ──
    articles_html = "<h2 style='color:#c8a96e;margin-top:32px;'>📰 Top Articles Today</h2>"
    for source in articles_df["source"].unique():
        source_df = articles_df[articles_df["source"] == source].head(3)
        articles_html += f"<h3 style='margin-top:20px;color:#0a0a0a;'>{source}</h3>"
        for _, row in source_df.iterrows():
            articles_html += f"""
            <div style='margin:8px 0;padding:10px 16px;background:#f5f0e8;'>
                <a href='{row['link']}' style='color:#0a0a0a;text-decoration:none;font-weight:bold;'>{row['title']}</a>
            </div>"""

    # ── FULL EMAIL ──
    html = f"""
    <html>
    <body style='font-family:Georgia,serif;max-width:600px;margin:0 auto;color:#0a0a0a;'>
        <div style='border-bottom:3px double #0a0a0a;padding:20px 0;text-align:center;margin-bottom:24px;'>
            <h1 style='font-size:32px;margin:0;'>Fashion <em style='color:#c8a96e;'>Intel</em></h1>
            <p style='color:#8a8278;font-size:12px;letter-spacing:2px;text-transform:uppercase;margin:6px 0 0;'>Daily Digest & Trend Alerts</p>
        </div>

        {alerts_html}
        {articles_html}

        <div style='border-top:1px solid #e0d8cc;margin-top:32px;padding-top:16px;font-size:11px;color:#8a8278;text-align:center;'>
            Fashion Intel System · Auto-generated daily digest
        </div>
    </body>
    </html>
    """
    return html


def send_email(alerts, articles_df):
    """Sends the daily digest + alerts email via Mailtrap"""

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"👗 Fashion Intel — {len(alerts)} Trend Alerts Today"
    msg["From"]    = SENDER_EMAIL
    msg["To"]      = RECEIVER_EMAIL

    html_body = build_email_body(alerts, articles_df)
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP(MAILTRAP_HOST, MAILTRAP_PORT) as server:
            server.login(MAILTRAP_USERNAME, MAILTRAP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print(f"[Email] ✅ Digest sent — {len(alerts)} alerts included")

    except Exception as e:
        print(f"[Email] ❌ Error: {e}")