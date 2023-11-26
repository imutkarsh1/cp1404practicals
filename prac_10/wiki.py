import wikipedia

while True:
    query = input("Enter a page title or search phrase (or press enter to exit): ")
    if query == "":
        break

    try:
        page = wikipedia.page(query, auto_suggest=False)
        print("\nPage Title:", page.title)
        print("\nSummary:", page.summary)
        print("\nURL:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation error. Please be more specific or choose from the following options:")
        for option in e.options:
            print(option)
    except wikipedia.exceptions.PageError:
        print("Page not found. Please try a different search term.")
    except Exception as e:
        print("An error occurred: ", str(e))

    print("\n" + "-"*80 + "\n")
