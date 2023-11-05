import requests

# Make a API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept" : "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Covert the responce object to dictionary.
responce_dict = r.json()

# Process results.
print(responce_dict.keys())