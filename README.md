# TextSmart

### Objective:
- Python microservice to summarize and categorize text documents using NLP techniques.

### Features:
- Accepts input via a text file (--input) and outputs JSON (--output).
- Cleans text: removes stopwords and punctuation.
- Summarizes text: extracts top 3 sentences.
- Categorizes text based on keywords: Finance, Sports, Technology, Health, Other.
- Includes logging and error handling.

### Usage:
- python -m textsmart.cli --input report.txt --output result.json

### Requirements:
- Python 3.10+
- Libraries: nltk, argparse
- NLTK data: punkt, stopwords
  
### Notes:
- Docker and unit tests were not included due to time and environment constraints.
- The core functionality (cleaning, summarization, categorization) has been implemented and tested
