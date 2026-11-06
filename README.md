# B2B Lead Scraper & Data Extractor

A robust, modular Python web scraper engineered for extracting structured business leads and directory listings with built-in anti-detection mechanics, randomized jitter delays, and clean multi-format export (CSV, JSON).

---

## ⚡ Key Architecture & Features

- **Anti-Detection Engine:** Randomized User-Agent cycling and human-like jitter delays (2-5s) to prevent IP rate-limiting.
- **Resilient Parsing:** CSS selector fallback logic to handle layout variations gracefully.
- **Export Formats:** Direct export to clean CSV and formatted JSON ready for CRM ingestion.
- **Lightweight & Fast:** Uses pure Python HTTP clients and BeautifulSoup without excessive memory footprint.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **BeautifulSoup4** (DOM parsing)
- **Urllib / Requests** (HTTP pipeline)
- **Pandas / CSV** (Data structuring and normalization)

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/b2b-lead-scraper.git
cd b2b-lead-scraper

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python main.py
```

---

## 📊 Sample Output Schema (CSV/JSON)

```json
{
  "business_name": "Apex Dental Clinic",
  "category": "Healthcare / Dentistry",
  "phone": "+1-555-0199",
  "website": "https://apexdentalexample.com",
  "rating": 4.9,
  "reviews_count": 142,
  "scraped_at": "2026-11-05T20:00:00Z"
}
```
