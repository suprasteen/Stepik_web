from flask import Flask, request, render_template
from time import time
import random

app = Flask(__name__)
videos = {
    1: {"id": "8KiFwL2aVUE", "title": "Философия - Ницше", "tags": ['Ницше', 'Нигилизм']},
    2: {"id": "pp1A3JePcYk", "title": "Восточная философия - Будда", "tags": ['Будда', 'Буддизм']},
    3: {"id": "AKtj8I5r4MQ", "title": "Философия - Эпикур", "tags": ['Эпикур']},
    4: {"id": "8qclKWVQiwY", "title": "Экзистенциализм и Эссенциализм", "tags": ['Сартр', 'Экзистенциализм', 'Свобода воли']},
    5: {"id": "m6Pqji7Vf_U", "title": "Взгляды на смерть", "tags": ['Смерть', 'Сократ', 'Эпикур', 'Чжуан-цзы']},
    6: {"id": "QS6o2dT2RWY", "title": "Утилитаризм", "tags": ['Утилитаризм']},
    7: {"id": "uNCUhDjscU4", "title": "Аристотель и Учение о Добродетелях", "tags": ['Аристотель']},
    8: {"id": "F-6BlgL0K4s", "title": "Теория общественного договора", "tags": ['Обществознание']},
    9: {"id": "ozQn7QCWJZo", "title": "Детерминизм против Свободы Воли", "tags": ['Детерминизм', 'Сознание', 'Свобода воли']},
    10: {"id": "d7mK7Lk9kx0", "title": "Кант и Категорический Императив", "tags": ['Кант']},
    11: {"id": "KshafAmECAo", "title": "Что такое философия", "tags": ['Истоки']},
    12: {"id": "kaTcHGqRYnM", "title": "Философия - Иммануил Кант", "tags": ['Кант']},
    13: {"id": "tKEfhma71rk", "title": "Философия - Альбер Камю", "tags": ['Смерть']},
    14: {"id": "vNqkUtrxeRw", "title": "Философия сознания: Свобода воли и детерминизм", "tags": ['Детерминизм', 'Сознание', 'Свобода воли']},
    15: {"id": "kKaE9pkVYPs", "title": "Философия - Мишель Фуко", "tags": ['Фуко']},
    16: {"id": "rrr3OIkhYdc", "title": "Просветление", "tags": ['Осознание', 'Просветление']},
    17: {"id": "q_uACV5kxQg", "title": "Восточная Философия - Кинцуги", "tags": ['Кинцуги']},
    18: {"id": "wRYYYN20vzE", "title": "Восточная Философия - Лао-цзы", "tags": ['Лао-цзы']},
    19: {"id": "UVZaEUWAf5A", "title": "Ницше: Сверхчеловек", "tags": ['Ницше', 'Сверхчеловек']},
    20: {"id": "CudOAUtcs8w", "title": "Платон: Миф о пещере", "tags": ['Платон', 'Бытие']},
    21: {"id": "pTZ2SWtqICI", "title": "Иисус, как философ доброты", "tags": ['Иисус']},
    22: {"id": "Ww86dGzOy-A", "title": "Смысл Жизни", "tags": ['Смысл жизни']},
#    23: {"id": "uNCUhDjscU4", "title": "м", "tags": []}

}
list_id_videos = list(range(1, len(videos) + 1))
link_base = "http://youtu.be/"

playlists = {
    1: {
        "title": "Европейская философия",
        "videos": [1, 4, 10, 12, 13, 15, 19]
    },
    2: {
        "title": "Восточная философия",
        "videos": [2, 17, 18]
    },
    3: {
        "title": "Древнегреческая философия",
        "videos": [3, 7]
    },

}


@app.route('/')
def main():
    title_page = "Главная"
    random_id = []
    while len(random_id) != 6:
        random_number = random.randrange(1, len(videos) + 1, 1)
        if random_number not in random_id:
            random_id.append(random_number)
    print(random_id)
    return render_template('index.html', videos = videos, random_id = random_id, playlists = playlists, title_page = title_page)

@app.route('/search/')
def search():
    title_page = "Поиск"
    search_result = []
    search = request.values.get('input_search').lower()
    for video_id in list_id_videos:
        for word_title in videos[video_id]["title"].lower().split():
            if search == word_title:
                search_result.append(video_id)
        for tag in videos[video_id]["tags"]:
            if search == tag.lower() and video_id not in search_result:
                search_result.append(video_id)
    random_id = []
    while len(random_id) != 3:
        random_number = random.randrange(1,len(videos)+1,1)
        if random_number not in random_id:
            random_id.append(random_number)
    print(random_id)
    len_result = len(search_result)
    return render_template('search.html', videos = videos, search_result = search_result, search = search, len_result = len_result, random_id = random_id, playlists = playlists, title_page = title_page )

@app.route('/videos/')
def videos_page():
    title_page = "Библиотека"
    return render_template('videos.html', videos = videos, playlists = playlists, title_page = title_page)

@app.route('/videos/<video_id>')
def videos_page_id(video_id):
    title_page = f"{videos[int(video_id)]['title']}"
    return render_template('video_page.html', videos = videos, playlists = playlists, video_id = int(video_id), link_base = link_base, title_page = title_page)

@app.route('/playlists/<playlist_id>')
def print_playlist(playlist_id):
    return render_template('playlist.html', videos = videos, playlists = playlists, playlist_id = playlist_id)
app.run('0.0.0.0',9090)