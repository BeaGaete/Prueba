import pandas as pd
import numpy as np


# retorna el minimo RSS con su punto de corte para la variable que se ingresa
def rss(dimpluspred, variablename):
    print(dimpluspred[variablename].values)
    rss_list =list()
    if len(dimpluspred[variablename].values) != 0:
        min = float(dimpluspred[variablename].values.min())
        max = float(dimpluspred[variablename].values.max())
        dominio = np.linspace(min, max, 1000)
        rss_list = list()
        for x in dominio:
            lesser_x = pd.DataFrame(columns=[variablename, 'PeriodLS'])
            greater_x = pd.DataFrame(columns=[variablename, 'PeriodLS'])
            for row in dimpluspred.iterrows():
                index, added_row = row
                if added_row[0] > x:
                    greater_x = pd.concat([greater_x, added_row.to_frame().T],
                                            ignore_index=True)
                else:
                    lesser_x = pd.concat([lesser_x, added_row.to_frame().T],
                                          ignore_index=True)
            greater_mean = greater_x['PeriodLS'].mean()
            lesser_mean = lesser_x['PeriodLS'].mean()
            suma_greater = sum(map(lambda y: (y - greater_mean)**2, greater_x['PeriodLS'].values))
            suma_lesser = sum(map(lambda y: (y - lesser_mean) ** 2,
                                   lesser_x['PeriodLS'].values))
            rss_list. append((x, round(suma_greater + suma_lesser, 2)))
    if len(rss_list) != 0:
        return sorted(rss_list, key=lambda y: y[1], reverse=True).pop()
    return rss_list




# con menos de k datos se termina el algoritmo
def finish_condition(data, n):
    if len(data.index) < n:
        return True
    return False

def get_cut_point(data):
    return data.mean()

def datatest_prediction(datatest, data):
    pass

def select_major_data(value):
    pass

def select_minor_data(value):
    pass


def regresion_tree(datatest, data, variables, n):
    if finish_condition(data, n):
        return datatest_prediction(datatest, data)
    else:
        variable = variables.pop()  # la variable con la menor varianza
        xd = data[variable]
        cut_point = get_cut_point(xd)
        xt = datatest[variable]
        if xt >= cut_point:
            data = select_major_data(cut_point)
        else:
            data = select_minor_data(cut_point)
        regresion_tree(datatest, data, variables, n)


