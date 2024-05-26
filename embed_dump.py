import os
import json
from read_epub import parse_book


def get_epub(dir):
    return [file for file in os.listdir(dir) if file.endswith('.epub') ]

def load_embed(epub_extension, modelname="mistral"):
    print("epubs: ", len(epub_extension))
    for filename in epub_extension:
        if not os.path.exists(f"embeddings/{filename}.json"):
            with open(f"embeddings/{filename}.json", "r") as f:
                chunks = parse_book(filename)
                print("chunks: " + len(chunks))
                emeddings= [ ollama.embeddings(model=modelname, prompt=chunk)["embedding"] for chunk in chunks]
                print("embeddings: ", len(embeddings))
                with open(f"embeddings/{filename}.json", "w") as f:
                    json.dump(embeddings, f)
def main():
    load_embed(get_epub('.'))

if __name__ == "__main__":
    main()
