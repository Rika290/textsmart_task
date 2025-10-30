CATEGORY_KEYWORDS = {
    "Finance": ["finance", "investment", "bank", "money", "revenue"],
    "Sports": ["sports", "game", "match", "tournament", "player"],
    "Technology": ["technology", "software", "AI", "machine learning", "tech"],
    "Health": ["health", "medical", "doctor", "hospital", "disease"]
}

def categorize_text(text: str) -> str:
    text_lower = text.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                return category
    return "Other"

