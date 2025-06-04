# 🎬 movie-cli

A simple, fast CLI tool to search for any movie using the [TMDb API](https://www.themoviedb.org/).  
Perfect for movie lovers who want quick results right in the terminal.

---

## ✨ Features

- 🔍 Search any movie by title
- 📅 See release year
- 🌐 Direct TMDb links for more info
- 💻 Lightweight and easy to use
- 🔐 Uses `.env` for secure API key handling

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Orange-Sreejon/movie-cli.git
cd movie-cli
```
### 2. (Optional) Create a virtual environment

```
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

## 🔐 Setup TMDb API Key

  1. Create an account at TMDb

  2. Go to API Settings and request a free API key

  3. Create a .env file in the project folder and add:

```
TMDB_API_KEY=your_api_key_here
```

✔️ .env is already ignored in .gitignore.


### 🚀 Usage

## Run the tool:

```
python movie_cli.py
```

Then enter a movie name when prompted:
```
Enter movie name: the dark knight
```

You'll see a list of results:

# 🧠 Tech Stack

> Python 3.10+

> requests

> python-dotenv

> TMDb API

## 🙌 Contributing

Pull requests and issues are welcome.
Feel free to fork and improve this project.

 📄 License

MIT License

Created with ❤️ by Orange-Sreejon
