import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("tmdb_api_key")

genre_response = requests.get(f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}')
data = genre_response.json()

genres = {}
for genre in data['genres']:
    genres[genre['id']] = genre['name']

response = requests.get(f'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&language=en-US&page=1&primary_release_date.gte=2023-01-01&vote_average.gte=5.5&with_genres=28&api_key={api_key}')
data = response.json()

for movie in data['results']:
    title = movie['title']
    overview = movie['overview']
    release_date = movie['release_date']
    genre_ids = movie['genre_ids']
    popularity = movie['popularity']
    vote_average = movie['vote_average']

    movie_genres = []
    for genre_id in genre_ids:
        movie_genres.append(genres[genre_id])

    keywords = []
    keywords_response = requests.get(f'https://api.themoviedb.org/3/movie/{movie["id"]}/keywords?api_key={api_key}')
    keywords_data = keywords_response.json()
    for keyword in keywords_data['keywords']:
        keywords.append(keyword['name'])

    reviews = []
    reviews_response = requests.get(f'https://api.themoviedb.org/3/movie/{movie["id"]}/reviews?api_key={api_key}')
    reviews_data = reviews_response.json()
    for review in reviews_data['results']:
        reviews.append(f"**Review by** {review['author']}\n\n" \
                       f"**Rating:** {review['author_details']['rating']}\n\n" \
                       f"{review['content']}\n\n---\n\n")

    markdown_text = f'# {title}\n\n' \
                    f'## Overview\n\n {overview}\n\n' \
                    f'## Details\n\n' \
                    f'**Release Date:** {release_date}\n\n' \
                    f'**Genres:** {", ".join(movie_genres)}\n\n' \
                    f'**Popularity:** {popularity}\n\n' \
                    f'**Vote Average:** {vote_average}\n\n' \
                    f'**Keywords:** {", ".join(keywords)}\n\n' \
                    f'## Reviews\n\n' \
                    f'{"".join(reviews)}' \
    
    with open(f'files/{title}.md', 'w') as f:
        f.write(markdown_text)