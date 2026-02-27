from flask import Flask, render_template, request
import random

app = Flask(__name__)

movies = [
    {
        "title": "Интерстеллар",
        "genre": "фантастика",
        "mood": "серьёзное",
        "year": "новый",
        "country": "США",
        "rating": 8.6,
        "description": "Команда исследователей отправляется через червоточину, чтобы спасти человечество.",
        "image": "../static/interstellar.jpg"
    },
    {
        "title": "1+1",
        "genre": "комедия",
        "mood": "весёлое",
        "year": "старый",
        "country": "Франция",
        "rating": 8.5,
        "description": "Трогательная и смешная история дружбы аристократа и парня из пригорода.",
        "image": "../static/1+1.jpg"
    },
    {
        "title": "Заклятие",
        "genre": "ужасы",
        "mood": "страшное",
        "year": "новый",
        "country": "США",
        "rating": 7.5,
        "description": "Супруги-экстрасенсы помогают семье, столкнувшейся с тёмной силой.",
        "image": "../static/zac.jpg"
    },
    {
        "title": "Титаник",
        "genre": "романтика",
        "mood": "грустное",
        "year": "старый",
        "country": "США",
        "rating": 7.9,
        "description": "История любви на борту легендарного затонувшего лайнера.",
        "image": "../static/titanic.jpg"
    },
    {
        "title": "Мстители: Финал",
        "genre": "боевик",
        "mood": "захватывающее",
        "year": "новый",
        "country": "США",
        "rating": 8.4,
        "description": "Герои собираются вместе, чтобы дать последний бой Таносу.",
        "image": "../static/mstiteli.jpg"
    },
    {
        "title": "Гарри Поттер",
        "genre": "фэнтези",
        "mood": "волшебное",
        "year": "старый",
        "country": "Великобритания",
        "rating": 8.2,
        "description": "Мальчик-волшебник учится в школе магии и сражается со злом.",
        "image": "../static/harri.jpg"
    },
    {
        "title": "Зелёная миля",
        "genre": "драма",
        "mood": "грустное",
        "year": "старый",
        "country": "США",
        "rating": 8.6,
        "description": "Надзиратель тюрьмы сталкивается с заключённым, обладающим сверхспособностями.",
        "image": "../static/green.jpg"
    },
    {
        "title": "Шрек",
        "genre": "мультфильм",
        "mood": "доброе",
        "year": "старый",
        "country": "США",
        "rating": 7.9,
        "description": "Огр отправляется в путешествие, чтобы спасти принцессу и находит друзей.",
        "image": "../static/shrec.jpg"
    }
]

# Главная страница
@app.route('/')
def index():
    trending = sorted(movies, key=lambda x: x["rating"], reverse=True)[:5]
    return render_template("index.html", trending=trending)

# Рекомендация по параметрам
@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form['genre']
    mood = request.form['mood']
    year = request.form['year']

    matching_movies = []

    for movie in movies:
        score = 0
        if movie["genre"] == genre:
            score += 1
        if movie["mood"] == mood:
            score += 1
        if movie["year"] == year:
            score += 1

        if score > 0:
            matching_movies.append((score, movie))

    if matching_movies:
        max_score = max(matching_movies, key=lambda x: x[0])[0]
        best_movies = [m[1] for m in matching_movies if m[0] == max_score]
        recommended_movies = best_movies[:6]
    else:
        recommended_movies = [{
            "title": "Фильмы не найдены",
            "genre": "-",
            "year": "-",
            "country": "-",
            "rating": "-",
            "description": "Попробуйте выбрать другие параметры.",
            "image": "not_found.jpg"
        }]

    trending = sorted(movies, key=lambda x: x["rating"], reverse=True)[:5]
    return render_template("result.html", movies=recommended_movies)

# Случайный фильм
@app.route('/random')
def random_movie():
    movie = random.choice(movies)
    trending = sorted(movies, key=lambda x: x["rating"], reverse=True)[:5]
    return render_template("result.html", movies=[movie])

if __name__ == "__main__":
    app.run(debug=True)