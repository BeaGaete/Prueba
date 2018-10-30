import numpy as np
import pandas as pd
import random
from functions import rss
pd.set_option('display.max_columns', None)

#####################################################
#                                                   #
#               nombre de columnas                  #
#                                                   #
#####################################################

# variable a predecir 'PeriodLS' posicion 46 de esta lista

COLUMNS = ['Amplitude', 'AndersonDarling', 'Autocor_length', 'Class', 'Con',
       'Eta_e', 'FluxPercentileRatioMid20', 'FluxPercentileRatioMid35',
       'FluxPercentileRatioMid50', 'FluxPercentileRatioMid65',
       'FluxPercentileRatioMid80', 'Freq1_harmonics_amplitude_0',
       'Freq1_harmonics_amplitude_1', 'Freq1_harmonics_amplitude_2',
       'Freq1_harmonics_amplitude_3', 'Freq1_harmonics_rel_phase_0',
       'Freq1_harmonics_rel_phase_1', 'Freq1_harmonics_rel_phase_2',
       'Freq1_harmonics_rel_phase_3', 'Freq2_harmonics_amplitude_0',
       'Freq2_harmonics_amplitude_1', 'Freq2_harmonics_amplitude_2',
       'Freq2_harmonics_amplitude_3', 'Freq2_harmonics_rel_phase_0',
       'Freq2_harmonics_rel_phase_1', 'Freq2_harmonics_rel_phase_2',
       'Freq2_harmonics_rel_phase_3', 'Freq3_harmonics_amplitude_0',
       'Freq3_harmonics_amplitude_1', 'Freq3_harmonics_amplitude_2',
       'Freq3_harmonics_amplitude_3', 'Freq3_harmonics_rel_phase_0',
       'Freq3_harmonics_rel_phase_1', 'Freq3_harmonics_rel_phase_2',
       'Freq3_harmonics_rel_phase_3', 'ID', 'LinearTrend', 'MaxSlope', 'Mean',
       'Meanvariance', 'MedianAbsDev', 'MedianBRP', 'N', 'PairSlopeTrend',
       'PercentAmplitude', 'PercentDifferenceFluxPercentile', 'PeriodLS',
       'Period_fit', 'Psi_CS', 'Psi_eta', 'Q31', 'Rcs', 'Skew',
       'SlottedA_length', 'SmallKurtosis', 'Std']

STRINGS = ['MIRA_SR', 'RRAB']




class Serie:

    # son 200669 filas
    # 20% de las filas son 40133.8 filas
    def __init__(self, file):
        self.raw_dataframe = pd.read_csv(file, sep=',')
        self.traindf = pd.DataFrame(columns=COLUMNS)
        self.testdf = pd.DataFrame(columns=COLUMNS)
        self.variance = dict()

    # obtenemos el dataframe de entrenamiento y el de prueba
    def get_set_train_test(self):
        contador = 0
        dotest = True
        for row in self.raw_dataframe.iterrows():
            index, added_row = row
            if dotest:
                if random.randint(0,1):
                    self.testdf = pd.concat([self.testdf, added_row.to_frame().T],
                                            ignore_index=True)
                else:
                    self.traindf = pd.concat([self.traindf, added_row.to_frame().T],
                                            ignore_index=True)
            else:
                self.traindf = pd.concat([self.traindf, added_row.to_frame().T],
                                         ignore_index=True)
            if len(self.testdf.index) == 40134:
                dotest = False
            contador += 1
            if contador == 1000:
                break
            """self.testdf.append(self.raw_dataframe.iloc[[test_list[i]]])
            print(self.testdf.iloc[[test_list[i]]])
        for i in range(0, len(self.testdf.index)):
            self.raw_dataframe.drop(self.testdf.iloc[[test_list[i]]])
        self.traindf = self.raw_dataframe"""

    # la menor varianza se saca con pop
    def get_variance(self):
        self.variance = sorted([(k, v) for k, v in self.traindf.var().to_dict(
        ).items()], key=lambda x: x[1], reverse=True)





if __name__ == "__main__":
    s = Serie("FATS_GAIA.dat")
    s.get_set_train_test()
    s.get_variance()
    #print(s.variance)
    #print(s.traindf[:5].iloc[:,46]) #s.traindf.iloc[:,46] variable a predecir
    #print(s.traindf['PeriodLS'].values)
    #print(type(s.traindf['PeriodLS'].values))
    #print(s.traindf['PeriodLS'].values.max())
    #print(s.traindf['PeriodLS'].values.min())
    #print(s.traindf['PeriodLS'].min)
    #print(s.traindf.iloc[:5][['Mean', 'PeriodLS']])
    #print(s.traindf.iloc[:5][['PeriodLS']].mean())
    lista_variable_RSS = list()
    for variable in COLUMNS:
        if variable != 'PeriodLS':
            df = s.traindf.iloc[:5][[variable, 'PeriodLS']]
            df = df[~df[variable].isin(STRINGS)]
            #df = pd.to_numeric(df[[variable, 'PeriodLS']], errors='coerce')
            #df.dropna(subset=[variable, 'PeriodLS'])
            lista_variable_RSS.append((variable, rss(df, variable)))
            print("terminamos una variable")
    print(lista_variable_RSS)
    #list_RSS_sort = sorted(
        #lista_variable_RSS, key=lambda x: x[1][1], reverse=True)
    #print(list_RSS_sort.pop())