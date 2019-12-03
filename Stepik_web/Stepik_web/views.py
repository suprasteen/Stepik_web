from flask import Flask, request, render_template
from time import time

app = Flask(__name__)
flavicon_ = '<link rel="icon" href="https://stepik.org/favicon.ico" type="image/x-icon">'
intro = '''<h1>Привет, это Stepik Existence. Портал видео о философии.</h1><br>
<a href="/videos/">Посмотреть видео</a><br><br>
<a href="/tags/">Посмотреть список тегов.</a><br><br>
<a href="/playlists/">Посмотреть список плейлистов.</a><br><br>
<a href="/search/">Найти видео.</a><br><br>
<a href="/about/">О проекте.</a><br><br>
'''
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

def print_videos():
    list_videos = []
    for video_id in list_id_videos:
        list_videos.append(video_id)
    return video_selection(list_videos)

def video_selection(list_videos):
    count = 0
    ppp = f'{flavicon_}<title>Видео</title><br><a href="/">На главную</a><br><br>'
    for sample_id in list_videos:
        count += 1
        ppp += f'''{count}. <a href="/videos/{sample_id}">{videos[sample_id]["title"]}</a> <br><br>'''
    return ppp

@app.route('/')
def main():
   return f'{flavicon_}<title>Главная</title>{intro}'

@app.route('/about/')
def about():
    return f'{flavicon_}<title>О проекте</title><br><a href="/">На главную</a><br><br>На проекте представлены все грани бытия. Сборник важнейших, в истории человечества, взглядов на Истину.'

@app.route('/videos/')
def list_video():
    return f'{flavicon_}<title>Видео</title>{print_videos()}'

@app.route('/videos/<id>/')
def video(id):
    id = int(id)
    link_tags = ""
    for tag in (videos[id]["tags"]):
        link_tags += f'<a href="/tags/{tag}/">{tag}</a>   '
    return  f'''{flavicon_}<br><title>Видео</title><a href="/">На главную</a><br><br>
    <h3>Название: {videos[id]["title"]}<br><br>
    Теги: {link_tags}<br><br>
    Ссылка: <a href="{link_base}{videos[id]["id"]}">{link_base}{videos[id]["id"]}</h3></a>'''

@app.route('/playlists/')
def print_list_playlists():
    ppp = f'{flavicon_}<br><title>Плейлисты</title><a href="/">На главную</a><br><br>'
    for playlist in playlists:
        ppp += f'{playlist}. <a href="/playlists/{playlist}">{playlists[playlist]["title"]}</a><br><br>'
    return ppp

@app.route('/playlists/<list>/')
def playlist(list):
    list = int(list)
    list_videos = playlists[list]["videos"]
    return f'{flavicon_}<title>{playlists[list]["title"]}</title>{video_selection(list_videos)}'

@app.route('/tags/')
def print_tags():
    tags = []
    string_tags = '<title>Теги</title>'
    for video_id in list_id_videos:
        for tag in videos[video_id]["tags"]:
            if tag not in tags:
                tags.append(tag)
    count_tags = 0
    for tag in tags:
        count_tags += 1
        string_tags += f'<a href="/tags/{tag}">{tag}</a> '
        if count_tags == 10:
            string_tags += '<br><br>'
            count_tags = 0
    string_tags = f'{flavicon_}<br><a href="/">На главную</a><br><br><h3>' + string_tags + '</h3>'
    return string_tags

@app.route('/tags/<tag>/')
def thetag(tag):
    video_tag = []
    for video_id in list_id_videos:
        for tag_ in videos[video_id]["tags"]:
            if tag == tag_:
                video_tag.append(video_id)
    return video_selection(video_tag)

@app.route('/search/')
def search_form():
    return render_template('search.html')

@app.route('/search/', methods=['POST'])
def run_search():
    tic = time()
    search_result = []
    search = request.form['text']
    for video_id in list_id_videos:
        for word_title in videos[video_id]["title"].lower().split():
            if search == word_title:
                search_result.append(video_id)
    if len(search_result) != 0:
        if len(search_result) % 10 == 1:
            result = ["найден", "результат"]
        elif 2 <= len(search_result) % 10 <= 4:
            result = ["найдено", "результата"]
        else:
            result = ["найдено", "результатов"]
        print()
    else:
        return (f'{flavicon_}По запросу "{search}" ничего не найдено. Повторите попытку.<br><br>{search_form()}')
    toc = time()
    return f'{flavicon_}По запросу "{search}" {result[0]} {len(search_result)} {result[1]} за {toc - tic} сек:<br><br>{search_form()}<br>{video_selection(search_result)}'

@app.errorhandler(404)
def page_not_found(error):
   return "<br><br><a href='/'>Главная</a><br><br><h2>Страница не найдена</h2>"

app.run('0.0.0.0',9090)