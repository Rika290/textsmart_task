import logging
import argparse
import json
from textsmart.modules.clean import clean_text
from textsmart.modules.summarize import summarize_text
from textsmart.modules.categorize import categorize_text

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    parser = argparse.ArgumentParser(description="TextSmart CLI")
    parser.add_argument("--input", type=str, required=True, help="Input text file")
    parser.add_argument("--output", type=str, required=True, help="Output JSON file")
    args = parser.parse_args()

    try:
        # Reads input file
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()
        if not text.strip():
            logging.error("Input file is empty.")
            return

        # Cleans the text
        cleaned_text = clean_text(text)

        # Summarize and categorize
        summary = summarize_text(cleaned_text)
        category = categorize_text(cleaned_text)

        # Prepare JSON output
        result = {
            "original_text": text,
            "cleaned_text": cleaned_text,
            "summary": summary,
            "category": category
        }

        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)

        logging.info(f"Result saved to {args.output}")

    except FileNotFoundError:
        logging.error(f"File {args.input} not found.")
    except UnicodeDecodeError:
        logging.error(f"Encoding issue with file {args.input}.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main() 
