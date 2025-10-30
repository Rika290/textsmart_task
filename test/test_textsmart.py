from textsmart.modules.clean import clean_text
from textsmart.modules.summarize import summarize_text
from textsmart.modules.categorize import categorize_text

def test_clean():
    text = "Hello, World!"
    cleaned = clean_text(text)
    assert cleaned == "hello world"  # adjust according to your function

def test_summarize():
    text = "Sentence one. Sentence two is longer. Sentence three."
    summary = summarize_text(text)
    assert len(summary) == 3

def test_categorize():
    text = "The bank approved my finance loan."
    category = categorize_text(text)
    assert category == "Finance"

