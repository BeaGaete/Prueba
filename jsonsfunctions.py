from functools import reduce
import json
import os
import collections


def gen(deq, copias, it):
    while True:
        if not deq:
            nuevo = next(it)
            for d in copias:
                d.append(nuevo)
        yield deq.popleft()

def gen_copias(iterable, n):
    it = iter(iterable)
    copias = [collections.deque() for _ in range(n)]
    return tuple(gen(d, copias, it) for d in copias)


def get_jsons_TV_Movie(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # tvmovie si
    TV_Movie_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'TV Movie' and float(x[7]) >= 11, g1)))
    TV_Movie_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'TV Movie' and float(x[7]) < 11, g2)))

    # tvmovie no
    TV_Movie_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'TV Movie' and float(x[7]) >= 11, g3)))
    TV_Movie_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'TV Movie' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = TV_Movie_YES_P
    dic1["popularity-"] = TV_Movie_YES_p
    dic2["popularity+"] = TV_Movie_NO_P
    dic2["popularity-"] = TV_Movie_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    TV_MOVIE = {"TV Movie": dic}
    #print(json.dumps(TV_MOVIE))
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'TV_MOVIE' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(TV_MOVIE, file)


def get_jsons_Science_Fiction(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Science_Fiction si
    Science_Fiction_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Science Fiction' and float(x[7]) >= 11, g1)))
    Science_Fiction_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Science Fiction' and float(x[7]) < 11, g2)))

    # Science_Fiction no
    Science_Fiction_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Science Fiction' and float(x[7]) >= 11, g3)))
    Science_Fiction_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Science Fiction' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Science_Fiction_YES_P
    dic1["popularity-"] = Science_Fiction_YES_p
    dic2["popularity+"] = Science_Fiction_NO_P
    dic2["popularity-"] = Science_Fiction_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Science_Fiction = {"Science Fiction": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Science Fiction' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Science_Fiction, file)

        'Documentary'

def get_jsons_Documentary(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Documentary si
    Documentary_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1,filter(
       lambda x: x[1] == 'Documentary' and float(x[7]) >= 11, g1)))
    Documentary_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1,filter(
        lambda x: x[1] == 'Documentary' and float(x[7]) < 11, g2)))

    # Documentary no
    Documentary_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1,filter(
        lambda x: x[1] != 'Documentary' and float(x[7]) >= 11,g3)))
    Documentary_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1,filter(
        lambda x: x[1] != 'Documentary' and float(x[7]) < 11,g4)))
    dic1["popularity+"] = Documentary_YES_P
    dic1["popularity-"] = Documentary_YES_p
    dic2["popularity+"] = Documentary_NO_P
    dic2["popularity-"] = Documentary_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Documentary = {"Documentary": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Documentary' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Documentary, file)


def get_jsons_Music(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Music si
    Music_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Music' and float(x[7]) >= 11, g1)))
    Music_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Music' and float(x[7]) < 11, g2)))

    # Music no
    Music_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Music' and float(x[7]) >= 11, g3)))
    Music_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Music' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Music_YES_P
    dic1["popularity-"] = Music_YES_p
    dic2["popularity+"] = Music_NO_P
    dic2["popularity-"] = Music_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Music = {"Music": dic}
    #print(json.dumps(TV_MOVIE))
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Music' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Music, file)


def get_jsons_Family(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Family si
    Family_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Family' and float(x[7]) >= 11, g1)))
    Family_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Family' and float(x[7]) < 11, g2)))

    # Family no
    Family_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Family' and float(x[7]) >= 11, g3)))
    Family_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Family' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Family_YES_P
    dic1["popularity-"] = Family_YES_p
    dic2["popularity+"] = Family_NO_P
    dic2["popularity-"] = Family_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Family = {"TV Movie": dic}
    #print(json.dumps(TV_MOVIE))
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Family' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Family, file)


def get_jsons_Comedy(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Comedy si
    Comedy_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Comedy' and float(x[7]) >= 11, g1)))
    Comedy_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Comedy' and float(x[7]) < 11, g2)))

    # Comedy no
    Comedy_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Comedy' and float(x[7]) >= 11, g3)))
    Comedy_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Comedy' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Comedy_YES_P
    dic1["popularity-"] = Comedy_YES_p
    dic2["popularity+"] = Comedy_NO_P
    dic2["popularity-"] = Comedy_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Comedy = {"Comedy": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Comedy' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Comedy, file)


def get_jsons_Mystery(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Mystery si
    Mystery_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Mystery' and float(x[7]) >= 11, g1)))
    Mystery_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Mystery' and float(x[7]) < 11, g2)))

    # Mystery no
    Mystery_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Mystery' and float(x[7]) >= 11, g3)))
    Mystery_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Mystery' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Mystery_YES_P
    dic1["popularity-"] = Mystery_YES_p
    dic2["popularity+"] = Mystery_NO_P
    dic2["popularity-"] = Mystery_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Mystery = {"Mystery": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Mystery' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Mystery, file)



def get_jsons_Crime(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Crime si
    Crime_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Crime' and float(x[7]) >= 11, g1)))
    Crime_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Crime' and float(x[7]) < 11, g2)))

    # Crime no
    Crime_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Crime' and float(x[7]) >= 11, g3)))
    Crime_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Crime' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Crime_YES_P
    dic1["popularity-"] = Crime_YES_p
    dic2["popularity+"] = Crime_NO_P
    dic2["popularity-"] = Crime_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Crime = {"Crime": dic}
    #print(json.dumps(TV_MOVIE))
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Crime' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Crime, file)


'Western'
def get_jsons_Western(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Western si
    Western_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Western' and float(x[7]) >= 11, g1)))
    Western_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Western' and float(x[7]) < 11, g2)))

    # Western no
    Western_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Western' and float(x[7]) >= 11, g3)))
    Western_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Western' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Western_YES_P
    dic1["popularity-"] = Western_YES_p
    dic2["popularity+"] = Western_NO_P
    dic2["popularity-"] = Western_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Western = {"Western": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Western' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Western, file)


def get_jsons_Thriller(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Thriller si
    Thriller_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Thriller' and float(x[7]) >= 11, g1)))
    Thriller_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Thriller' and float(x[7]) < 11, g2)))

    # Thriller no
    Thriller_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Thriller' and float(x[7]) >= 11, g3)))
    Thriller_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Thriller' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Thriller_YES_P
    dic1["popularity-"] = Thriller_YES_p
    dic2["popularity+"] = Thriller_NO_P
    dic2["popularity-"] = Thriller_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Thriller = {"Thriller": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Thriller' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Thriller, file)


def get_jsons_Foreign(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Foreign si
    Foreign_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Foreign' and float(x[7]) >= 11, g1)))
    Foreign_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Foreign' and float(x[7]) < 11, g2)))

    # Foreign no
    Foreign_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Foreign' and float(x[7]) >= 11, g3)))
    Foreign_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Foreign' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Foreign_YES_P
    dic1["popularity-"] = Foreign_YES_p
    dic2["popularity+"] = Foreign_NO_P
    dic2["popularity-"] = Foreign_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Foreign = {"Foreign": dic}
    #print(json.dumps(TV_MOVIE))
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Foreign' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Foreign, file)


def get_jsons_Drama(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Drama si
    Drama_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Drama' and float(x[7]) >= 11, g1)))
    Drama_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Drama' and float(x[7]) < 11, g2)))

    # Drama no
    Drama_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Drama' and float(x[7]) >= 11, g3)))
    Drama_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Drama' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Drama_YES_P
    dic1["popularity-"] = Drama_YES_p
    dic2["popularity+"] = Drama_NO_P
    dic2["popularity-"] = Drama_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Drama = {"Drama": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Drama' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Drama, file)


def get_jsons_Animation(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Animation si
    Animation_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Animation' and float(x[7]) >= 11, g1)))
    Animation_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Animation' and float(x[7]) < 11, g2)))

    # Animation no
    Animation_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Animation' and float(x[7]) >= 11, g3)))
    Animation_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Animation' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Animation_YES_P
    dic1["popularity-"] = Animation_YES_p
    dic2["popularity+"] = Animation_NO_P
    dic2["popularity-"] = Animation_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Animation = {"Animation": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Animation' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Animation, file)


def get_jsons_Action(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Action si
    Action_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Action' and float(x[7]) >= 11, g1)))
    Action_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Action' and float(x[7]) < 11, g2)))

    # Action no
    Action_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Action' and float(x[7]) >= 11, g3)))
    Action_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Action' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Action_YES_P
    dic1["popularity-"] = Action_YES_p
    dic2["popularity+"] = Action_NO_P
    dic2["popularity-"] = Action_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Action = {"Action": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Action' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Action, file)


def get_jsons_War(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # War si
    War_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'War' and float(x[7]) >= 11, g1)))
    War_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'War' and float(x[7]) < 11, g2)))

    # War no
    War_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'War' and float(x[7]) >= 11, g3)))
    War_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'War' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = War_YES_P
    dic1["popularity-"] = War_YES_p
    dic2["popularity+"] = War_NO_P
    dic2["popularity-"] = War_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    War = {"War": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'War' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(War, file)


def get_jsons_Fantasy(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Fantasy si
    Fantasy_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Fantasy' and float(x[7]) >= 11, g1)))
    Fantasy_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Fantasy' and float(x[7]) < 11, g2)))

    # Fantasy no
    Fantasy_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Fantasy' and float(x[7]) >= 11, g3)))
    Fantasy_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Fantasy' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Fantasy_YES_P
    dic1["popularity-"] = Fantasy_YES_p
    dic2["popularity+"] = Fantasy_NO_P
    dic2["popularity-"] = Fantasy_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Fantasy = {"Fantasy": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Fantasy' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Fantasy, file)


def get_jsons_Adventure(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Adventure si
    Adventure_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Adventure' and float(x[7]) >= 11, g1)))
    Adventure_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Adventure' and float(x[7]) < 11, g2)))

    # Adventure no
    Adventure_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Adventure' and float(x[7]) >= 11, g3)))
    Adventure_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Adventure' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Adventure_YES_P
    dic1["popularity-"] = Adventure_YES_p
    dic2["popularity+"] = Adventure_NO_P
    dic2["popularity-"] = Adventure_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Adventure = {"Adventure": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Adventure' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Adventure, file)


def get_jsons_History(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # History si
    History_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'History' and float(x[7]) >= 11, g1)))
    History_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'History' and float(x[7]) < 11, g2)))

    # History no
    History_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'History' and float(x[7]) >= 11, g3)))
    History_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'History' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = History_YES_P
    dic1["popularity-"] = History_YES_p
    dic2["popularity+"] = History_NO_P
    dic2["popularity-"] = History_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    History = {"History": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'History' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(History, file)


def get_jsons_Horror(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Horror si
    Horror_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Horror' and float(x[7]) >= 11, g1)))
    Horror_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Horror' and float(x[7]) < 11, g2)))

    # Horror no
    Horror_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Horror' and float(x[7]) >= 11, g3)))
    Horror_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Horror' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Horror_YES_P
    dic1["popularity-"] = Horror_YES_p
    dic2["popularity+"] = Horror_NO_P
    dic2["popularity-"] = Horror_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Horror = {"Horror": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Horror' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Horror, file)


def get_jsons_Romance(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    g1, g2, g3, g4 = gen_copias(gen_movies, 4)
    # Romance si
    Romance_YES_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Romance' and float(x[7]) >= 11, g1)))
    Romance_YES_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] == 'Romance' and float(x[7]) < 11, g2)))

    # Romance no
    Romance_NO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Romance' and float(x[7]) >= 11, g3)))
    Romance_NO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: x[1] != 'Romance' and float(x[7]) < 11, g4)))
    dic1["popularity+"] = Romance_YES_P
    dic1["popularity-"] = Romance_YES_p
    dic2["popularity+"] = Romance_NO_P
    dic2["popularity-"] = Romance_NO_p
    dic["YES"] = dic1
    dic["NO"] = dic2
    Romance = {"Romance": dic}
    if not os.path.isdir('json/genre'):
        os.makedirs('json/genre')
    with open("json/genre/" + 'Romance' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(Romance, file)


def get_jsons_budget(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    dic3 = dict()
    g1, g2, g3, g4, g5, g6 = gen_copias(gen_movies, 6)
    budget_ALTO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: int(x[3]) > 10000000 and float(x[7]) >= 11, g1)))
    budget_MEDIO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: int(x[3]) >= 1000000 and int(x[3]) <= 10000000 and float(x[7]) >= 11, g2)))
    budget_BAJO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: int(x[3]) < 1000000 and float(x[7]) >= 11, g3)))

    budget_ALTO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: int(x[3]) > 10000000 and float(x[7]) < 11, g4)))
    budget_MEDIO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: int(x[3]) >= 1000000 and int(x[3]) <= 10000000 and float(x[7]) < 11, g5)))
    budget_BAJO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: int(x[3]) < 1000000 and float(x[7]) < 11, g6)))

    dic1["popularity+"] = budget_ALTO_P
    dic1["popularity-"] = budget_ALTO_p
    dic2["popularity+"] = budget_MEDIO_P
    dic2["popularity-"] = budget_MEDIO_p
    dic3["popularity+"] = budget_BAJO_P
    dic3["popularity-"] = budget_BAJO_p
    dic["ALTO"] = dic1
    dic["MEDIO"] = dic2
    dic["BAJO"] = dic3
    budget = {"budget": dic}
    if not os.path.isdir('json/budget'):
        os.makedirs('json/budget')
    with open("json/budget/" + 'budget' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(budget, file)


def get_jsons_revenue(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    dic3 = dict()
    g1, g2, g3, g4, g5, g6 = gen_copias(gen_movies, 6)
    revenue_ALTO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: float(x[4]) > 60000000 and float(x[7]) >= 11, g1)))
    revenue_MEDIO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: float(x[4]) >= 10000000 and float(x[4]) <= 60000000 and float(x[7]) >= 11, g2)))
    revenue_BAJO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: float(x[4]) < 10000000 and float(x[7]) >= 11, g3)))

    revenue_ALTO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: float(x[4]) > 60000000 and float(x[7]) < 11, g4)))
    revenue_MEDIO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: float(x[4]) >= 10000000 and float(x[4]) <= 60000000 and float(x[7]) < 11, g5)))
    revenue_BAJO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: float(x[4]) < 10000000 and float(x[7]) < 11, g6)))

    dic1["popularity+"] = revenue_ALTO_P
    dic1["popularity-"] = revenue_ALTO_p
    dic2["popularity+"] = revenue_MEDIO_P
    dic2["popularity-"] = revenue_MEDIO_p
    dic3["popularity+"] = revenue_BAJO_P
    dic3["popularity-"] = revenue_BAJO_p
    dic["ALTO"] = dic1
    dic["MEDIO"] = dic2
    dic["BAJO"] = dic3
    revenue = {"revenue": dic}
    if not os.path.isdir('json/revenue'):
        os.makedirs('json/revenue')
    with open("json/revenue/" + 'revenue' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(revenue, file)


def get_jsons_date(gen_movies):
    dic = dict()
    dic1 = dict()
    dic2 = dict()
    dic3 = dict()
    g1, g2, g3, g4, g5, g6 = gen_copias(gen_movies, 6)
    date_ALTO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: int(x[6].split('-')[2]) > 0 and float(x[7]) >= 11, g1)))
    date_MEDIO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: int(x[6]) >= 10000000 and int(x[6].split('-')[2])  and float(x[7]) >= 11, g2)))
    date_BAJO_P = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: int(x[6]) < 10000000 and float(x[7]) >= 11, g3)))

    date_ALTO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: int(x[6]) > 60000000 and float(x[7]) < 11, g4)))
    date_MEDIO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: int(x[6]) >= 10000000 and int(x[6]) <= 60000000 and float(x[7]) < 11, g5)))
    date_BAJO_p = reduce(lambda x, y: x + y, map(lambda x: 1, filter(
        lambda x: int(x[6]) < 10000000 and float(x[7]) < 11, g6)))

    dic1["popularity+"] = date_ALTO_P
    dic1["popularity-"] = date_ALTO_p
    dic2["popularity+"] = date_MEDIO_P
    dic2["popularity-"] = date_MEDIO_p
    dic3["popularity+"] = date_BAJO_P
    dic3["popularity-"] = date_BAJO_p
    dic["ALTO"] = dic1
    dic["MEDIO"] = dic2
    dic["BAJO"] = dic3
    date = {"date": dic}
    if not os.path.isdir('json/date'):
        os.makedirs('json/date')
    with open("json/date/" + 'date' + '.json', 'w',
              encoding="utf-8") as file:
        json.dump(date, file)
