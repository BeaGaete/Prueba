import pandas as pd
from functools import reduce
from graphics import *
import numpy as np
import json
from pprint import pprint


PATH1 = "datasets/Programación Avanzada.csv"
PATH2 = "datasets/Arquitectura de Computadores.json"
NAVALUES = ["#N/A", "#N/A N/A", "#NA", "-1.#IND", "-1.#QNAN", "-NaN", "-nan",
"1.#IND", "1.#QNAN", "N/A", "NA", "NULL", "NaN", "n/a", "nan", "null"]
COLOR1 = '#15959F'
COLOR2 = '#F26144'


class ProgramacionAvanzada:

    def __init__(self, path1, filename):
        self.path = path1
        self.data = pd.read_csv(self.path, header=0, delim_whitespace=False,
                                na_values=NAVALUES)
        self._array = list()
        self.chart = Chart(self.data, filename)


    # retorna todas las notas de un alumno en un semestre

    def get_df(self):
        dataf = pd.DataFrame(self.data)
        return dataf[(dataf.nota != "P")]

    """def notas_semestre_an_o_alumno(self, an_o, sem, al):
        df = pd.DataFrame(self.data)
        return df[(df.nota != "P") & (df.semestre == sem) & (
            df.ano == an_o) & (df.alumno == al)]"""

    # recibe dataframe de un alumno en un semestre
    def nota_final_alumno(self, df):
        act = self._select_act(df)
        tar = self._select_tar(df)
        notas_act = act.ix[:, 4]
        notas_tar = tar.ix[:, 4]

        # tengo que quitar el mínimo

        suma_notas_act = notas_act.map(lambda x: float(x)).sum()
        suma_notas_tar = notas_tar.map(lambda x: float(x)).sum()
        prom_act = suma_notas_act/4
        prom_tar = suma_notas_tar/6
        return float("{0:.3f}".format(0.5 * prom_act + 0.5 * prom_tar, 3))

    # UserWarning: This pattern has match groups. To actually get the groups, use str.extract
    def _select_act(self, df):
        return df[df.evaluacion.str.contains('^(AC)')]

    def _select_tar(self, df):
        return df[df.evaluacion.str.contains('^(T)')]

    def get_graphics_points(self, lista):
        # an_o, semestre, alumno, evaluacion, nota
        dic = {}
        # e[0] es año semestre
        for e in lista[:99]:
            key = str(e[1][0]) + "-" + str(e[1][1])
            if not dic.get(key, False):
                dic[key] = list()
                dic[key].append(e[0])
            else:
                dic[key].append(e[0])
            # print(dic[key])
            """if not dic[e[0]].get(e[1], False):
                    dic[e[0]][e[1]] = list()
                    dic[e[0]][e[1]].append(e[2])
                else:
                    dic[e[0]][e[1]].append(e[2])"""
        #for k, v in dic:
            #print(k, (sum(dic[k])/len(dic[k])))


    def set_array(self):
        no_ordenados = list()
        for e in self.get_df().groupby(['ano', 'semestre']): # son 10 e
            lista = list()
            for ee in e[1].groupby(['alumno']):
                dataframe = ee[1] # dataframe alumno semestre año
                lista.append(self.nota_final_alumno(dataframe))
            suma_notas_sem = reduce(lambda x, y: float(x) + float(y), lista)
            no_ordenados.append((round(
                suma_notas_sem/len(lista), 2), e[0], np.std(lista)))
            # print(no_ordenados)
        self._array = no_ordenados
        """i = 9
        while i >= 2:
            self._array.append(no_ordenados[i])
            self._array.append(no_ordenados[i-1])
            i -= 2
        self._array.append(no_ordenados[i])
        self._array.append(no_ordenados[i - 1])"""

    def get_array(self):
        return self._array



    """def _variance(self):
        lista = list()
        for i in range(10):
            lista.append(self.agrupar()[i][0])
        return np.var(lista)
        # notas = [map(lambda x: x[0], self.agrupar())]
        # return notas
        #return self._normalizacion(np.var([1, 2, 3]))"""

class SVGchart:

    def __init__(self, pa, ac):
        self.pa = pa
        self.ac = ac
        self.chart = Chart("chart.svg")

    def _normalizacion(self, nota):
        return ((nota - 1)/(7 - 1)) * (700 - 100) + 100

    def draw_points(self, color1, color2):
        for i in range(10):
            self.chart.draw_circles(140 + i*120, 750 - self._normalizacion(
                self.pa.get_array()[i][0]), color1)
            self.chart.draw_circles(140 + i * 120, 750 - self._normalizacion(
                self.ac.get_array()[i][0]), color2)

    def draw_variances(self, color1, color2):
        for i in range(10):
            nota = self._normalizacion(self.pa.get_array()[i][0])
            desviacion = self._normalizacion(self.pa.get_array()[i][2])
            self.chart.draw_variance(start=(
                140 + i*120, 750 - (nota + desviacion)), end=(
                140 + i*120, 750 - (nota - desviacion)), color=color1)
            nota = self._normalizacion(self.ac.get_array()[i][0])
            desviacion = self._normalizacion(self.ac.get_array()[i][2])
            self.chart.draw_variance(
                start=(140 + i * 120, 750 - (nota + desviacion)),
                end=(140 + i * 120, 750 - (nota - desviacion)), color=color2)

    def draw_grid(self):
        for i in range(7):
            self.chart.draw_line_h(750 - self._normalizacion(i + 1))
        for i in range(10):
            self.chart.draw_line_v(140 + i * 120)

    def draw_polyline(self, color1, color2):
        for i in range(9):
            nota1 = self._normalizacion(self.pa.get_array()[i][0])
            nota2 = self._normalizacion(self.pa.get_array()[i + 1][0])
            self.chart.draw_poly(start=(140 + i*120, 750 - nota1),
                                 end=(140 + (i + 1)*120, 750 - nota2), color=color1)
            nota1 = self._normalizacion(self.ac.get_array()[i][0])
            nota2 = self._normalizacion(self.ac.get_array()[i + 1][0])
            self.chart.draw_poly(start=(140 + i * 120, 750 - nota1),
                                 end=(140 + (i + 1) * 120, 750 - nota2), color=color2)

    def add_texts(self):
        for i in range(10):
            texto = self.pa.get_array()[i][1]
            # print(texto) # texto[0] + "-" + texto[1]
            self.chart.add_text(str(texto[0]) + "-" + str(texto[1]), insert=(
                140 + i * 120, 770))
            if i <= 6:
                self.chart.add_text(str(i + 1), insert=(
                    30, 755 - self._normalizacion(i + 1)))


class ArquiComputadores:
    def __init__(self):
        self.data = None
        self._array = list()

    # 919 alumnos
    def get_df(self):
        with open("datasets/Arquitectura de Computadores.json", "r") as f:
            rawstring = f.read()
        dic = json.loads(rawstring) # dic es un diccionario
        new_dic = {}
        for k, v in dic.items():
            if not "P" in v["interrogaciones"] and not "P" in v[ # hay 57 datos con nota P
                "proyecto"] and not "P" in v["tareas"]:
                v["interrogaciones"] = sum(map(lambda x: round(float(x.replace(
                    ",", ".")), 2), v["interrogaciones"]))/len(v["interrogaciones"])
                v["proyecto"] = sum(map(lambda x: round(float(x.replace(
                    ",", ".")), 2), v["proyecto"]))/len(v["proyecto"])
                v["tareas"] = sum(map(lambda x: round(float(x.replace(
                    ",", ".")), 2), v["tareas"]))/len(v["tareas"])
                v["nota_final"] = 0.3 * v["interrogaciones"] + 0.4 * v["proyecto"] + 0.3 * v["tareas"]
                del v["interrogaciones"]
                del v["proyecto"]
                del v["tareas"]
                new_dic[k] = v
        self.data = pd.DataFrame(new_dic).transpose()
        # print(self.data)
        return self.data


    def nota_prom_semestre_sd(self, df):
        notas = df.ix[:, 1]
        prom = round(notas.map(lambda x: x).sum()/len(df.index), 2)
        sd = np.std(notas.map(lambda x: x))
        return prom, sd

    def set_array(self):
        for e in self.data.groupby(['ano', 'semestre']):
            par = self.nota_prom_semestre_sd(e[1])
            self._array.append((par[0], e[0], par[1]))
        return self._array

    def get_array(self):
        return self._array


# alumno   ano  semestre evaluacion nota

if __name__ == '__main__':
    pa = ProgramacionAvanzada(PATH1, "chart.svg")
    # data =
    # df = pd.DataFrame(data)
    # notas_no_p = df[(df.nota != "P") & (df.semestre == 1) & (df.ano == 2014)]
    # an_o = df_an_o[df_an_o.ano != "P"]
    # semestre = data.ix[:, 2]
    # evaluacion = data.ix[:, 3]
    # nota = data.ix[:, 4]
    # notas = pa.notas_semestre_an_o_alumno(2014, 1, 235)
    # print(pa._select_act(notas))
    # print(notas)
    # print(pa.nota_final_alumno(notas)) #pa.nota_final_alumno(notas)
    """lista = [["2014-2", "1", "AC", 4.5], ["2014-2", "1", "T", 6],
             ["2014-2", "1", "AC", 3.6], ["2014-2", "2", "T", 4.8],
             ["2014-2", "2", "AC", 3.9], ["2014-2", "3", "T", 4.2],
             ["2014-2", "3", "T", 6.7], ["2014-1", "45", "T", 3.6],
             ["2014-1", "45", "AC", 2.6], ["2014-1", "8", "AC", 5.2],
             ["2014-1", "8", "T", 5.2], ["2013-2", "6", "T", 5.0]]"""
    # print(pa.join_marks_by_semester(lista))
    # plt.plot(nota, an_o)
    pa.set_array()
    lista = pa.get_array()
    #[print(n) for n in lista]


    ac = ArquiComputadores()
    ac.get_df()
    ac.set_array()
    #print(ac.data)
    lista = ac.get_array()
    # [print(n) for n in lista]
    #print(ac.set_array())
    #print(lista)
    #pa.get_graphics_points(lista)
    chart = SVGchart(pa, ac)
    chart.chart.dwg.viewbox(width=WIDTH, height=HEIGHT)
    chart.chart.draw_axes()
    chart.add_texts()
    # print(pa.variance())
    chart.chart.draw_rectangle()
    chart.draw_grid()
    chart.draw_polyline(COLOR1, COLOR2)
    chart.draw_variances(COLOR1, COLOR2)  # 'blue', 'red'
    chart.draw_points(COLOR1, COLOR2)
    chart.chart.dwg.save()



