import wikipedia

def search_wiki(query):
    try:
        summary = wikipedia.summary(query, sentences=3)
        print(f"\n Wikipedia Summary for '{query}':\n")
        print(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Too many results: {e.options[:5]}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Wikipedia Search Tool")
    q = input("Enter a topic to search: ")
    search_wiki(q)
