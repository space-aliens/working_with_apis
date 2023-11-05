import requests
import plotly.express as px

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

repo_names, stars = [], []


for repo_dict in repo_dicts:
   repo_names.append(repo_dict['name'])
   stars.append(repo_dict['stargazers_count'])


# Make Visualization
title = "Most-Starred Python Projects on GitHub."
labels = {'x':'Repository', 'y':'Stars'}

fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()