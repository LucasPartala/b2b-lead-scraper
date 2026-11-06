"""
B2B Lead Scraper & Data Extractor
Author: Lucas Partala
Description: Modular Python scraper for extracting structured business data.
"""

import csv
import json
import random
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import List, Optional
import urllib.request
from bs4 import BeautifulSoup

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]

@dataclass
class BusinessLead:
    business_name: str
    category: str
    phone: str
    website: str
    rating: float
    reviews_count: int
    scraped_at: str

class B2BLeadScraper:
    def __init__(self, delay_range: tuple = (1.5, 3.5)):
        self.delay_range = delay_range
        self.session_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        }

    def _get_headers(self) -> dict:
        headers = self.session_headers.copy()
        headers["User-Agent"] = random.choice(USER_AGENTS)
        return headers

    def _jitter_delay(self):
        sleep_time = random.uniform(*self.delay_range)
        time.sleep(sleep_time)

    def extract_sample_leads(self) -> List[BusinessLead]:
        """Simulates structured lead generation pipeline."""
        self._jitter_delay()
        now = datetime.utcnow().isoformat() + "Z"
        
        sample_data = [
            BusinessLead("Nova Dental Studio", "Dentist", "+1-305-555-0142", "https://novadentalexample.com", 4.9, 128, now),
            BusinessLead("Apex Plumbing Solutions", "Plumber", "+1-305-555-0189", "https://apexplumbingexample.com", 4.8, 94, now),
            BusinessLead("Vanguard Logistics LLC", "Freight & Logistics", "+1-305-555-0199", "https://vanguardlogexample.com", 4.7, 62, now),
        ]
        return sample_data

    def export_csv(self, leads: List[BusinessLead], filepath: str = "leads_output.csv"):
        if not leads:
            return
        keys = asdict(leads[0]).keys()
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows([asdict(lead) for lead in leads])
        print(f"[OK] Exported {len(leads)} leads to {filepath}")

    def export_json(self, leads: List[BusinessLead], filepath: str = "leads_output.json"):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump([asdict(lead) for lead in leads], f, indent=2, ensure_ascii=False)
        print(f"[OK] Exported {len(leads)} leads to {filepath}")

if __name__ == "__main__":
    print("[*] Initializing B2B Lead Scraper...")
    scraper = B2BLeadScraper()
    leads = scraper.extract_sample_leads()
    scraper.export_csv(leads)
    scraper.export_json(leads)
    print("[*] Extraction pipeline completed successfully.")
