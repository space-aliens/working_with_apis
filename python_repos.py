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
print(f"Total repositories: {responce_dict['total_count']}")
print(f"Complete results: {not responce_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = responce_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dicts)}")



print(f"\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Description: {repo_dict['description']}")
    print(f"Repository: {repo_dict['html_url']}")