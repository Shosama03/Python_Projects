from exa_py import Exa
exa = Exa("d73395c7-bd62-4d43-9aae-a2ee65b37f93")

query = input("Search here: ")

response = exa.search(
    query,
    num_results = 5,
    type = "keyword",
    include_domains=["https://www.youtube.com/"]
)

for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
    print()
