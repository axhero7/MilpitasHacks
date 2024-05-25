import os
import json
from read_epub import parse_book

def get_epub(dir):
    return [file.endswith('.epub') for file in os.listdir(dir)]

def load_embed(epub_extension, modelname="mistral"):
    for filename in epub_extension:
        with open(f"embeddings/{filename}.json", "r") as f:
            chunk = parse_book(filename)
            emeddings= [ ollama.embeddings(model=modelname, prompt=chunk)["embedding"] for chunk in chunks]
            with open(f"embeddings/{filename}.json", "w") as f:
                json.dump(embeddings, f)
def main():
    load_embed(get_epub('.'))

