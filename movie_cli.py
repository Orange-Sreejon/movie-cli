from dotenv import load_dotenv
import os

import requests

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
DETAILS_URL = "https://api.themoviedb.org/3/movie/{}"

def search_movies(query):
    params = {"api_key": API_KEY, "query": query}
    res = requests.get(SEARCH_URL, params=params)
    return res.json().get("results", [])

def get_movie_details(movie_id):
    params = {"api_key": API_KEY, "append_to_response": "external_ids"}
    res = requests.get(DETAILS_URL.format(movie_id), params=params)
    return res.json()

def main():
    query = input("🎬 Search movie: ").strip()
    if not query:
        print("❌ No input.")
        return

    results = search_movies(query)
    if not results:
        print("❌ No results found.")
        return

    for i, movie in enumerate(results[:10], 1):
        title = movie["title"]
        year = movie.get("release_date", "")[:4]
        rating = movie.get("vote_average", "N/A")
        print(f"{i}. {title} ({year}) - ⭐ {rating}")

    try:
        choice = int(input("👉 Pick number: "))
        if choice < 1 or choice > len(results[:10]):
            print("❌ Invalid choice.")
            return
    except ValueError:
        print("❌ Not a number.")
        return

    movie_id = results[choice - 1]["id"]
    details = get_movie_details(movie_id)
    imdb_id = details.get("external_ids", {}).get("imdb_id")
    imdb_link = f"https://www.imdb.com/title/{imdb_id}/" if imdb_id else "N/A"

    print("\n🎞️  Movie Details")
    print("Title:", details.get("title", "N/A"))
    print("Release:", details.get("release_date", "N/A"))
    print("Runtime:", details.get("runtime", "N/A"), "min")
    print("Rating:", details.get("vote_average", "N/A"))
    print("Overview:", details.get("overview", "N/A"))
    print("IMDb:", imdb_link)

if __name__ == "__main__":
    main()
