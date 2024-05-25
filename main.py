import ollama
from read_epub import parse_book
import os
import json


def save_embedding(path, embeddings):
    if not os.path.exists("embeddings"):
        os.makedirs("embeddings")
    with open(f"embeddings/{path}.json", "w") as f:
        json.dump(embeddings, f)
def load_embedding(path):
    if not os.path.exists(f"embeddings/{filename}.json"):
        return False
    with open(f"embeddings/{filename}.json", "r") as f:
        return json.load(f)
def create_embedding(filepath, model_id, chunks):
    if (embeddings := load_embedding(filepath)) is not False:
        return embeddings
    embeddings = [ollama.embeddings(model=model_id, prompt=chunk)['embedding'] for chunk in chunks]
    save_embedding(filepath, embeddings)
    return embeddings

def main():
    filename = "batman_test.epub"
    paragraphs = parse_book(filename)
    embeddings = create_embedding(filename, "llama3", paragraphs)
    print(len(embeddings))

if __name__ == "__main__":
    main()
