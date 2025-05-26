import json
import requests
from typing import Dict, List, Optional

# Local fallback static map (same as before)
ICON_DB_LOCAL = {
    "city": {"icon": "city", "library": "Font Awesome", "url": "https://fontawesome.com/icons/city?s=solid"},
    "wifi": {"icon": "wifi", "library": "Font Awesome", "url": "https://fontawesome.com/icons/wifi?s=solid"},
    "smart": {"icon": "microchip", "library": "Font Awesome", "url": "https://fontawesome.com/icons/microchip?s=solid"},
    "signal": {"icon": "signal", "library": "Font Awesome", "url": "https://fontawesome.com/icons/signal?s=solid"},
    "traffic": {"icon": "traffic-light", "library": "Font Awesome", "url": "https://fontawesome.com/icons/traffic-light?s=solid"},
    "home": {"icon": "house", "library": "Font Awesome", "url": "https://fontawesome.com/icons/house?s=solid"},
    "car": {"icon": "car", "library": "Font Awesome", "url": "https://fontawesome.com/icons/car?s=solid"},
    "cloud": {"icon": "cloud", "library": "Font Awesome", "url": "https://fontawesome.com/icons/cloud?s=solid"},
    "robot": {"icon": "robot", "library": "Font Awesome", "url": "https://fontawesome.com/icons/robot?s=solid"},
    "iot": {"icon": "satellite-dish", "library": "Font Awesome", "url": "https://fontawesome.com/icons/satellite-dish?s=solid"},
}

class IconMapper:
    def __init__(self, 
                 icon_db_local: Dict[str, Dict] = ICON_DB_LOCAL,
                 icon_db_url: Optional[str] = None,
                 fetch_timeout: float = 2.0):
        """
        :param icon_db_local: Local fallback icon dictionary.
        :param icon_db_url: URL to fetch remote icon JSON db.
        :param fetch_timeout: Seconds before request timeout.
        """
        self.icon_db_local = icon_db_local
        self.icon_db_url = icon_db_url
        self.fetch_timeout = fetch_timeout
        self.icon_db_remote = None
        self.icon_db = self._load_icon_db()

    def _load_icon_db(self) -> Dict[str, Dict]:
        if not self.icon_db_url:
            print("No remote URL provided; using local icon DB.")
            return self.icon_db_local
        
        try:
            print(f"Fetching icon DB from {self.icon_db_url} with timeout {self.fetch_timeout}s...")
            resp = requests.get(self.icon_db_url, timeout=self.fetch_timeout)
            resp.raise_for_status()
            icon_db_remote = resp.json()
            if isinstance(icon_db_remote, dict):
                self.icon_db_remote = icon_db_remote
                print("Successfully loaded remote icon DB.")
                return icon_db_remote
            else:
                print("Remote icon DB JSON invalid format, falling back to local.")
        except Exception as e:
            print(f"Failed to fetch remote icon DB: {e}. Falling back to local.")
        
        return self.icon_db_local

    def get_matching_icons(self, keywords: List[str]) -> List[Dict]:
        icons = []
        for keyword in keywords:
            if keyword in self.icon_db:
                icons.append(self.icon_db[keyword])
            else:
                print(f"⚠️ No icon match found for keyword: {keyword}")
        return icons

