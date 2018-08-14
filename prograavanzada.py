import pandas as pd
import matplotlib.pyplot as plt


PATH1 = "datasets/Programación Avanzada.csv"
PATH2 = "datasets/Arquitectura de Computadores.json"
NAVALUES = ["#N/A", "#N/A N/A", "#NA", "-1.#IND", "-1.#QNAN", "-NaN", "-nan",
"1.#IND", "1.#QNAN", "N/A", "NA", "NULL", "NaN", "n/a", "nan", "null"]


class ProgramacionAvanzada:

    def __init__(self, path1):
        self.path = path1
        self.data = pd.read_csv(self.path, header=0, delim_whitespace=False,
                                na_values=NAVALUES)


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
            print(dic[key])
            """if not dic[e[0]].get(e[1], False):
                    dic[e[0]][e[1]] = list()
                    dic[e[0]][e[1]].append(e[2])
                else:
                    dic[e[0]][e[1]].append(e[2])"""
        #for k, v in dic:
            #print(k, (sum(dic[k])/len(dic[k])))

    # e es una tupla
    def agrupar(self):
        lista = list()
        for e in self.get_df().groupby(['ano', 'semestre']): # son 10 e
            for ee in e[1].groupby(['alumno']):
                dataframe = ee[1] # dataframe alumno semestre año
                lista.append((self.nota_final_alumno(dataframe), e[0]))
        return lista
                # print() # un alumno
                #print(type(e[])) # e[0] es (2016, 2), e[1] es un dataframe




# alumno   ano  semestre evaluacion nota

if __name__ == '__main__':
    pa = ProgramacionAvanzada(PATH1)
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
    lista = pa.agrupar()
    pa.get_graphics_points(lista)



