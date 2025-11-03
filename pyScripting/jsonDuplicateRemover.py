import json
import unicodedata
import os

def clean_title(title: str) -> str:
    """Normalize and clean book titles for deduplication."""
    return unicodedata.normalize('NFKC', title).strip().lower()

def load_books(filename: str):
    """Load a JSON file safely and return a list of book dictionaries."""
    with open(filename, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"{filename} has invalid JSON near line {e.lineno}, col {e.colno}: {e.msg}") from None
        
        # Handle case: {"books": [...]} or direct list
        if isinstance(data, dict):
            data = data.get('books', [])
        if not isinstance(data, list):
            raise ValueError(f"{filename} does not contain a list of books.")
        return data

def merge_books(file1, file2, output):
    books1 = load_books(file1)
    books2 = load_books(file2)

    merged = {
        clean_title(b.get('title', '')): b
        for b in books1 + books2
        if b.get('title')
    }

    merged_list = sorted(merged.values(), key=lambda x: clean_title(x['title']))

    with open(output, 'w', encoding='utf-8') as f:
        json.dump(merged_list, f, indent=2, ensure_ascii=False)

    print(f"✅ Merged {len(books1)} + {len(books2)} books → {len(merged_list)} unique entries.")
    print(f"📂 Output: {os.path.abspath(output)}")

if __name__ == "__main__":
    merge_books('book.json', 'bookc.json', 'finalBooks.json')
