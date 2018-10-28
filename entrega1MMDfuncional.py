import pandas as pd
import numpy as np
import json
import sqlite3
from functools import reduce
from jsonsfunctions import *
from algorythmfunctions import *
import collections
import os
import random
import time


GENRES = ["TV Movie", "Science Fiction", "Documentary", "Music", "Family",
          "Comedy", "Mystery", "Crime", "Western", "Thriller", "Foreign",
          "Drama", "Animation", "Action", "War", "Fantasy", "Adventure",
          "History", "Horror", "Romance"]

# las siguientes funciones transform y get transforman strings a numeros y
# obtienen en una lista los géneros, lenguajes y compañìas de las peliculas

def transform_budget(budget):
    return int(budget)


def transform_popularity(popularity):
    return float(popularity)  # replace("'", '"')


def transform_revenue(revenue):
    return float(revenue)


def transform_vote_average(vote_average):
    return float(vote_average)  # replace("'", '"')


def get_id(collection):
    string_list = collection.strip('[').strip(']').replace(
        "}, ", "};").replace("'", '"')
    newdic = json.loads(string_list)
    if newdic["id"]:
        return newdic["id"]
    return 0


def get_genres(genres):
    string_list = genres.strip('[').strip(']').replace("}, ", "};").replace(
        "'", '"').split(";")
    genres_list = list()
    for s in string_list:
        s.replace("'", '"')
        newdic = json.loads(s)
        genres_list.append(newdic["name"])
    return genres_list


def get_companies(companies):
    string_list = companies.strip('[').strip(']').replace("}, ", "};")\
        .replace("'", '"').split(";")
    companies_list = list()
    for s in string_list:
        s.replace("'", '"')
        newdic = json.loads(s)
        companies_list.append(newdic["name"])
    return companies_list


def get_languages(languages):
    string_list = languages.strip('[').strip(']').replace("}, ", "};")\
        .replace("'", '"').split(";")
    languages_list = list()
    for s in string_list:
        s.replace("'", '"')
        newdic = json.loads(s)
        languages_list.append(newdic["iso_639_1"])
    return languages_list


# dataframe donde se gyardan las peliculas
df = pd.DataFrame(
            columns=["title", "genre", "company", "budget", "revenue",
                     "language", "date", "popularity", "votes"])


# saca las filas corruptas del archivo csv y de las que se filtra se genera
# una copia por género lenguaje y compañía. Retorna una lista de listas
# es usada en la funcion abrir_movies_en_funcional
def clean_csv(lista):
    list_of_list = list()
    error = False
    budget = None
    genres = ['']
    companies = ['']
    revenue = None
    vote_average = None
    languages = ['']
    popularity = None
    count_error = 0
    for i in range(23):
        try:
            if i == 2 and lista[2] != '':
                budget = transform_budget(lista[2])
            elif i == 3 and lista[3] != '':
                genres = get_genres(lista[3])
            elif i == 10:
                popularity = transform_popularity(lista[10])
            elif i == 12 and lista[12] != '':
                companies = get_companies(lista[12])
            elif i == 15 and lista[15] != '':
                revenue = transform_revenue(lista[15])
            elif i == 17 and lista[17] != '':
                languages = get_languages(lista[17])
            elif i == 22 and lista[22] != '':
                vote_average = transform_vote_average(lista[22])
        except IndexError as err:
            error = True
            #count_error += 1
            #print("ERROR in line " + str(count))
        except json.decoder.JSONDecodeError as err:
            error = True
            #count_error += 1
            #print(err)
        except ValueError as err:
            error = True
            #count_error += 1
            #print(err)
        except TypeError as err:
            error = True
            #count_error += 1
            #print(err)
    if not error:
        for g in genres:
            for l in languages:
                for c in companies:
                    list_of_list.append([lista[8], g, c, str(budget), str(revenue), l,
                                         lista[14], str(popularity), str(vote_average)])
    return list_of_list


# abre el archivo .csv a través de un generador
def abrir_movies_en_funcional(text_file):
    with open(text_file, "r", encoding='utf-8',
              errors='ignore') as file:
        file.readline()
        movie = iter(file)
        n = next(movie)
        l = n.strip("\n").split(";")
        while True:
            yield l
            n = next(movie)
            l = n.strip("\n").split(";")




#################################################################
#                                                               #
#       las siguientes lineas se usaron para obtener            #
#       los géneros, lenguajes y compañías                      #
#                                                               #
#################################################################



count = 0
genres = set()
languages = set()
companies = set()

COLUMNS = ["title", "genre", "company", "budget", "revenue",
                     "language", "date", "popularity", "votes"]

class MoviesBD:
    def __init__(self):
        self.conn = sqlite3.connect('movies.db')
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS movies_table (movie_id TEXT, title TEXT, '
                       'genre TEXT, company TEXT, budget INTEGER, revenue REAL,'
                       ' language TEXT, date TEXT, popularity REAL, votes REAL, type_budget TEXT, type_revenue TEXT)')

    def budget_clasifier(self, budget):
        budget = int(budget)
        if budget > 10000000:
            return "A"
        elif budget >= 1000000 and budget <= 10000000:
            return "M"
        else:
            return "B"

    def revenue_clasifier(self, revenue):
        revenue = float(revenue)
        if revenue > 60000000:
            return "A"
        elif revenue >= 10000000 and revenue <= 60000000:
            return "M"
        else:
            return "B"

    def popularity_clasifier(self, pop):
        pop = float(pop)
        if pop > 11:
            return "A"
        else:
            return "B"

    def data_entry(self):
        count = 0
        for n in abrir_movies_en_funcional("movies_metadata.csv"):
            lista = clean_csv(n)
            if len(lista) != 0:
                for movie in lista:
                    count += 1
                    budget = self.budget_clasifier(movie[3])
                    revenue = self.revenue_clasifier(movie[4])
                    self.c.execute("INSERT INTO movies_table (movie_id, title, genre, company, budget, revenue, language, date, popularity, votes, type_budget, type_revenue) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (str(count), movie[0], movie[1], movie[2], movie[3], movie[4], movie[5], movie[6], movie[7], movie[8], budget, revenue))
        self.conn.commit()

    def get_json_movies(self):
        """cursor = self.c.execute(
            "SELECT m1.movie_id, m2.movie_id FROM movies_table as m1, movies_table "
            "as m2 WHERE m1.genre = m2.genre AND m1.type_budget = "
            "m2.type_budget OR m1.type_revenue = m2.type_revenue "
            "AND m1.title != m2.title GROUP BY m1.title")
        cont = 0
        for r in cursor:
            print(r)
            if cont == 1:
                break
            cont+= 1"""
        dic = dict()
        cursor = self.c.execute(
            "SELECT * FROM movies_table")
        for r in cursor:
            dic1 = dict()
            dic1["title"] = r[1]
            dic1["genre"] = r[2]
            dic1["company"] = r[3]
            dic1["budget"] = r[4]
            dic1["revenue"] = r[5]
            dic1["language"] = r[6]
            dic1["date"] = r[7]
            dic1["popularity"] = r[8]
            dic1["votes"] = r[9]
            dic1["type_budget"] = r[10]
            dic1["type_revenue"] = r[11]
            dic[r[0]] = dic1
        if not os.path.isdir('json/movies'):
            os.makedirs('json/movies')
        with open("json/movies/" + 'movies' + '.json', 'w',
                  encoding="utf-8") as file:
            json.dump(dic, file)

    def get_id_movies_attr(self):
        dic = dict()
        genre = collections.defaultdict(list)
        budget = collections.defaultdict(list)
        revenue = collections.defaultdict(list)
        cursor = self.c.execute("SELECT * FROM movies_table")
        for r in cursor:
            genre[r[2]].append(r[0])
            budget[r[10]].append(r[0])
            revenue[r[11]].append(r[0])
        if len(genre) > 10:
            dic["genre"] = genre
            #print(len(dic["genre"]))
            #print(dic["genre"])
        elif len(genre) <= 10:
            dic["genre"] = genre
        if len(budget) > 10:
            dic["budget"] = budget
        elif len(budget) <= 10:
            dic["budget"] = budget
        if len(revenue) > 10:
            dic["revenue"] = revenue
        elif len(revenue) <= 10:
            dic["revenue"] = revenue
        if not os.path.isdir('json/attr'):
            os.makedirs('json/attr')
        with open("json/attr/" + 'attr' + '.json', 'w',
                  encoding="utf-8") as file:
            json.dump(dic, file)

    # aqui obtenems os vecinos cercanos para todas las peliculas que cumplan
    # con igual género, tramo de budget y tramo de revenue
    """def get_nn(self):
        dic = dict()
        with open("json/attr/" + 'attr' + '.json', 'r',
                  encoding="utf-8") as attr:
            dic_attr = json.load(attr)
            with open("json/movies/" + 'movies' + '.json', 'r',
                  encoding="utf-8") as movies:
            dic_movies = json.load(movies)
            movies = self.abrir_new_movies('movies.csv')
            cont = 0
            for n in movies:
                dic1 = dict()
                #print(type(dic_attr["genre"][n[1]]))
                #print(dic_attr["genre"][n[1]])
                largo = len(dic_attr["genre"][n[1]])
                ids_genre = random.sample(dic_attr["genre"][n[1]], min(largo, 100))
                #print(dic_attr["genre"][n[1]])
                largo = len(dic_attr["budget"][n[9]])
                ids_budget = random.sample(dic_attr["budget"][n[9]], min(largo, 100))
                #print(ids_budget)
                largo = len(dic_attr["revenue"][n[10]])
                ids_revenue = random.sample(dic_attr["revenue"][n[10]], min(largo, 100))
                #print(ids_revenue)
                result = set(ids_genre).intersection(set(ids_budget)).intersection(set(
                    ids_revenue))
                #print(result)

                dic1["title"] = n[0]
                dic1["neigh"] = list(result)
                #print(dic1)
                if dic1 not in dic.values():
                    #print("deberia imprimir esto")
                    dic[str(cont)] = dic1
                cont += 1
                #print(dic)
                #time.sleep(2)

                if cont == 10000:
                    break
                print(cont)
            if not os.path.isdir('json/neigh'):
                os.makedirs('json/neigh')
            with open("json/neigh/" + 'neigh1' + '.json', 'w',
                      encoding="utf-8") as file:
                #print(dic)
                #time.sleep(2)
                json.dump(dic, file)

            movies = self.abrir_new_movies('movies.csv')
            cont = 0
            dic = dict()
            for n in movies:
                if cont >= 10000:
                    dic1 = dict()
                    largo = len(dic_attr["genre"][n[1]])
                    ids_genre = random.sample(dic_attr["genre"][n[1]], min(largo, 100))
                    # print(dic_attr["genre"][n[1]])
                    largo = len(dic_attr["budget"][n[9]])
                    ids_budget = random.sample(dic_attr["budget"][n[9]], min(largo, 100))
                    largo = len(dic_attr["revenue"][n[10]])
                    ids_revenue = random.sample(dic_attr["revenue"][n[10]], min(largo, 100))
                    result = set(ids_genre).intersection(
                        set(ids_budget)).intersection(set(ids_revenue))
                    dic1["title"] = n[0]
                    dic1["neigh"] = list(result)

                    if dic1 not in dic.values():
                        # print("deberia imprimir esto")
                        dic[str(cont)] = dic1
                cont += 1
                print(cont)
                if cont == 20000:
                    break
                print(cont)
            with open("json/neigh/" + 'neigh2' + '.json', 'w',
                      encoding="utf-8") as file:
                json.dump(dic, file)

            movies = self.abrir_new_movies('movies.csv')
            cont = 0
            dic = dict()
            for n in movies:
                if cont >= 20000:
                    dic1 = dict()
                    largo = len(dic_attr["genre"][n[1]])
                    ids_genre = random.sample(dic_attr["genre"][n[1]],
                                              largo // 2)
                    # print(dic_attr["genre"][n[1]])
                    largo = len(dic_attr["budget"][n[9]])
                    ids_budget = random.sample(dic_attr["budget"][n[9]],
                                               largo // 2)
                    largo = len(dic_attr["revenue"][n[10]])
                    ids_revenue = random.sample(dic_attr["revenue"][n[10]],
                                                largo // 2)
                    result = set(ids_genre).intersection(
                        set(ids_budget)).intersection(set(ids_revenue))
                    dic1["title"] = n[0]
                    dic1["neigh"] = list(result)

                    if dic1 not in dic.values():
                        # print("deberia imprimir esto")
                        dic[str(cont)] = dic1
                cont += 1
                print(cont)
                if cont == 30000:
                    break
                print(cont)
            with open("json/neigh/" + 'neigh3' + '.json', 'w',
                      encoding="utf-8") as file:
                json.dump(dic, file)

            movies = self.abrir_new_movies('movies.csv')
            cont = 0
            dic = dict()
            for n in movies:
                if cont >= 30000:
                    dic1 = dict()
                    largo = len(dic_attr["genre"][n[1]])
                    ids_genre = random.sample(dic_attr["genre"][n[1]],
                                              largo // 2)
                    # print(dic_attr["genre"][n[1]])
                    largo = len(dic_attr["budget"][n[9]])
                    ids_budget = random.sample(dic_attr["budget"][n[9]],
                                               largo // 2)
                    largo = len(dic_attr["revenue"][n[10]])
                    ids_revenue = random.sample(dic_attr["revenue"][n[10]],
                                                largo // 2)
                    result = set(ids_genre).intersection(
                        set(ids_budget)).intersection(set(ids_revenue))
                    dic1["title"] = n[0]
                    dic1["neigh"] = list(result)

                    if dic1 not in dic.values():
                        # print("deberia imprimir esto")
                        dic[str(cont)] = dic1
                cont += 1
                print(cont)
                if cont == 40000:
                    break
                print(cont)
            with open("json/neigh/" + 'neigh4' + '.json', 'w',
                      encoding="utf-8") as file:
                json.dump(dic, file)

            movies = self.abrir_new_movies('movies.csv')
            cont = 0
            dic = dict()
            for n in movies:
                if cont >= 50000:
                    dic1 = dict()
                    largo = len(dic_attr["genre"][n[1]])
                    ids_genre = random.sample(dic_attr["genre"][n[1]],
                                              largo // 2)
                    # print(dic_attr["genre"][n[1]])
                    largo = len(dic_attr["budget"][n[9]])
                    ids_budget = random.sample(dic_attr["budget"][n[9]],
                                               largo // 2)
                    largo = len(dic_attr["revenue"][n[10]])
                    ids_revenue = random.sample(dic_attr["revenue"][n[10]],
                                                largo // 2)
                    result = set(ids_genre).intersection(
                        set(ids_budget)).intersection(set(ids_revenue))
                    dic1["title"] = n[0]
                    dic1["neigh"] = list(result)

                    if dic1 not in dic.values():
                        # print("deberia imprimir esto")
                        dic[str(cont)] = dic1
                cont += 1
                print(cont)
            with open("json/neigh/" + 'neigh5' + '.json', 'w',
                      encoding="utf-8") as file:
                json.dump(dic, file)"""

    def gen_neighbours(self):
        with open("json/attr/" + 'attr' + '.json', 'r',
                  encoding="utf-8") as attr:
            dic_attr = json.load(attr)
            for g in GENRES:
                dic = dict()
                dic[g+"A"+"A"] = list(set(dic_attr["genre"][g]).intersection(set(dic_attr["budget"]["A"])).intersection(set(dic_attr["revenue"]["A"])))
                dic[g+"A"+"M"] = list(set(dic_attr["genre"][g]).intersection(set(dic_attr["budget"]["A"])).intersection(set(dic_attr["revenue"]["M"])))
                dic[g+"A"+"B"] = list(set(dic_attr["genre"][g]).intersection(set(dic_attr["budget"]["A"])).intersection(set(dic_attr["revenue"]["B"])))
                dic[g+"M"+"A"] = list(set(dic_attr["genre"][g]).intersection(set(dic_attr["budget"]["M"])).intersection(set(dic_attr["revenue"]["A"])))
                dic[g+"M"+"M"] = list(set(dic_attr["genre"][g]).intersection(set(dic_attr["budget"]["M"])).intersection(set(dic_attr["revenue"]["M"])))
                dic[g+"M"+"B"] = list(set(dic_attr["genre"][g]).intersection(set(dic_attr["budget"]["M"])).intersection(set(dic_attr["revenue"]["B"])))
                dic[g+"B"+"A"] = list(set(dic_attr["genre"][g]).intersection(set(dic_attr["budget"]["B"])).intersection(set(dic_attr["revenue"]["A"])))
                dic[g+"B"+"M"] = list(set(dic_attr["genre"][g]).intersection(set(dic_attr["budget"]["B"])).intersection(set(dic_attr["revenue"]["M"])))
                dic[g+"B"+"B"] = list(set(dic_attr["genre"][g]).intersection(set(dic_attr["budget"]["B"])).intersection(set(dic_attr["revenue"]["B"])))
                if not os.path.isdir('json/neigh'):
                    os.makedirs('json/neigh')
                with open("json/neigh/" + g + '.json', 'w', encoding="utf-8") as file:
                    json.dump(dic, file)

    def get_last_table(self):
        cursor1 = self.c.execute("SELECT * FROM movies_table")
        cursor2 = self.c.execute("SELECT * FROM movies_table")
        dic = dict()
        with open("json/movies/" + 'movies.json', 'r',
                  encoding="utf-8") as file:
            dic_movies = json.load(file)
        for r in dic_movies.keys():
            dic[r] = dict()
            dic[r]["num"] = 0
            dic[r]["aciertos"] = 0
            for s in cursor2:
                if s[0] != r:
                    #print((s[2] + s[10] + s[11]).replace("'", '"'))
                    #print(type(s[2] + s[10] + s[11]))
                    with open("json/neigh/" + s[2] + '.json', 'r',
                              encoding="utf-8") as file:
                        dic_attr = json.load(file)
                    for id in dic_attr[s[2] + s[10] + s[11]]:
                        if r == id:
                            dic[r]["num"] += 1
                            if self.popularity_clasifier(
                                    dic_movies[id]["popularity"]) == \
                                    self.popularity_clasifier(s[8]):
                                dic[r]["aciertos"] += 1
            print("fin de un r")
        if not os.path.isdir('json/weight'):
            os.makedirs('json/weight')
        with open("json/weight/" + "table" + '.json', 'w',
                  encoding="utf-8") as file:
            json.dump(dic, file)

    def get_new_last_table(self):
        dic = dict()
        with open("json/movies/" + 'movies.json', 'r',
                  encoding="utf-8") as file:
            dic_movies = json.load(file)
        cont = 0
        for ide in dic_movies.keys():
            dic[ide] = dict()
            dic[ide]["num"] = 0
            dic[ide]["aciertos"] = 0
            genre = dic_movies[ide]["genre"]
            type_b = dic_movies[ide]["type_budget"]
            type_r = dic_movies[ide]["type_revenue"]
            for g in GENRES:
                with open("json/neigh/" + g + '.json', 'r',
                          encoding="utf-8") as file:
                    dic_attr = json.load(file)
                for categoria, listas in dic_attr.items():
                    for id in listas:
                        if categoria == genre + type_b + type_r and ide != id:
                            dic[ide]["num"] += 1
                            if self.popularity_clasifier(dic_movies[ide][
                                "popularity"]) == self.popularity_clasifier(
                                dic_movies[id]["popularity"]):
                                dic[ide]["aciertos"] += 1
            cont += 1
            print(cont)
        if not os.path.isdir('json/weight'):
            os.makedirs('json/weight')
        with open("json/weight/" + "table" + '.json', 'w',
                  encoding="utf-8") as file:
            json.dump(dic, file)

    def calcular_distancia(self, k):
        with open("json/weight/" + "table" + '.json', 'r',
                  encoding="utf-8") as file:
            dic_table = json.load(file)
        dic_table[k]

    # como argumentos recibe el genero, categoria de budget y de revenue
    # de la película a partir de la cual se obtendran los vecinos más cercanos
    def serch_neighbours(self, genre, budget, revenue):
        with open("json/movies/" + 'movies.json', 'r',
                  encoding="utf-8") as file:
            dic_movies = json.load(file)

        for k in dic_movies.keys():
            if genre == dic_movies[k]["genre"] and budget == dic_movies[k][
                "type_budget"] and revenue == dic_movies[k]["type_revenue"]:
                pass
            elif genre == dic_movies[k]["genre"] and budget == dic_movies[k][
                "type_budget"]:
                pass
            elif genre == dic_movies[k]["genre"] and revenue == dic_movies[k][
                "type_revenue"]:
                pass
            elif budget == dic_movies[k][
                "type_budget"] and revenue == dic_movies[k]["type_revenue"]:
                pass






















    def create_new_csv(self):
        with open('movies.csv', 'w') as file:
            file.write(';'.join(COLUMNS) + ';' + 'type_budget' + ';' + 'type_revenue' + '\n')
            for n in abrir_movies_en_funcional("movies_metadata.csv"):
                lista = clean_csv(n)
                if len(lista) != 0:
                    for movie in lista:
                        if len(movie) == 9:
                            budget = self.budget_clasifier(movie[3])
                            revenue = self.revenue_clasifier(movie[4])
                            file.write(';'.join(movie) + ';' + budget + ';' + revenue + '\n')

    def abrir_new_movies(self, text_file):
        with open(text_file, "r", encoding='utf-8', errors='ignore') as file:
            file.readline()
            movie = iter(file)
            n = next(movie)
            l = n.strip("\n").split(";")
            while True:
                yield l
                n = next(movie)
                l = n.strip("\n").split(";")


    def create_jsons(self):
        gen_movies = self.abrir_new_movies("movies.csv")
        g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, \
        g17, g18, g19, g20, g21, g22 = gen_copias(gen_movies, 22)
        get_jsons_TV_Movie(g1)
        get_jsons_Science_Fiction(g2)
        get_jsons_Documentary(g3)
        get_jsons_Music(g4)
        get_jsons_Family(g5)
        get_jsons_Comedy(g6)
        get_jsons_Mystery(g7)
        get_jsons_Crime(g8)
        get_jsons_Western(g9)
        get_jsons_Thriller(g10)
        get_jsons_Foreign(g11)
        get_jsons_Drama(g12)
        get_jsons_Animation(g13)
        get_jsons_Action(g14)
        get_jsons_War(g15)
        get_jsons_Fantasy(g16)
        get_jsons_Adventure(g17)
        get_jsons_History(g18)
        get_jsons_Horror(g19)
        get_jsons_Romance(g20)
        get_jsons_budget(g21)
        get_jsons_revenue(g22)



if __name__ == "__main__":
    m = MoviesBD()
    # m.create_new_csv()
    """m.create_jsons()
    print(get_mvdm_genre('Crime'))
    print(get_mvdm_budget_alto_medio())
    print(get_mvdm_budget_bajo_medio())
    print(get_mvdm_budget_alto_bajo())
    print(get_mvdm_revenue_alto_medio())
    print(get_mvdm_revenue_bajo_medio())
    print(get_mvdm_revenue_alto_bajo())"""
    #m.create_table()
    #m.data_entry()
    # m.get_json_movies()
    # m.get_id_movies_attr()
    #m.gen_neighbours()
    m.get_new_last_table()





"""with open('movies.csv', 'w') as file:
    file.write(','.join(COLUMNS) + '\n')
    for n in abrir_movies_en_funcional("movies_metadata.csv"):
        lista = clean_csv(n)
        if len(lista) != 0:
            for movie in lista:
                count += 1
                file.write(','.join(movie) + '\n')

                #df.loc[count] = movie
    #print(count)
    #print(genres)
    #print(languages)
    #print(companies)"""



LANGUAGES = ['et', 'ka', 'sr', 'sq', 'ky', 'af', 'te', 'zh', 'eu', 'fa', 'hu',
             'dz', 'th', 'iu', 'vi', 'sv', 'cy', 'lo', 'nv', 'uz', 'bs', 'hi',
             'am', 'ro', 'ar', 'ku', 'ga', 'yi', 'sw', 'ca', 'sl', 'mr', 'ru',
             'ms', 'tg', 'tl', 'fi', 'ja', 'el', 'no', 'mn', 'cn', 'sk', 'ln',
             'bo', 'az', 'ny', 'ps', 'xx', 'kn', 'de', 'en', 'wo', 'ne', 'pl',
             'km', 'mi', 'tr', 'da', 'kk', 'id', 'fr', 'ur', 'rw', 'cr', 'ay',
             'so', 'ko', 'xh', 'ig', 'la', 'pa', 'sg', 'sh', 'ta', 'lv', 'sc',
             'ml', 'jv', 'st', 'cs', 'hy', 'ha', 'es', 'pt', 'mk', 'zu', 'ug',
             'hr', 'gu', 'bn', 'sm', 'sn', 'it', 'he', 'gn', 'my', 'mt', 'uk',
             'gl', 'tn', 'is', 'bg', 'nl', 'eo', 'lb', 'se', 'qu', 'bm', 'gd']

"SELECT m1.movie_id, m2.movie_id FROM movies_table as m1, movies_table as m2 WHERE m1.genre = m2.genre AND m1.type_budget = m2.type_budget OR m1.type_revenue = m2.type_revenue AND m1.title != m2.title GROUP BY m1.title"

