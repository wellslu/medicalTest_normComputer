import pandas as pd
import numpy as np


class Benson(object):
    def __init__(self):
        self.benson_data, self.benson_recall_data = self.prepare_raw_data()

    @staticmethod
    def prepare_raw_data():
        df = pd.read_excel(r'C:\Users\wells\PycharmProjects\vgh_flask\data\常模總整理.xlsx', sheet_name='Benson全')
        df.columns = df.loc[3, :]
        df = df[[df.columns[i] for i in range(13)]][:21]
        df = df[4:]
        df2 = pd.read_excel(r'C:\Users\wells\PycharmProjects\vgh_flask\data\常模總整理.xlsx', sheet_name='BensonRecall')
        df2.columns = df2.loc[3, :]
        df2 = df2[[df2.columns[i] for i in range(13)]][:21]
        df2 = df2[4:]
        return df, df2

    def measure(self, age=None, score=None, edu=None, test=None):
        if edu == '' or score == '' or age == '' or test == '':
            return '', '', ''
        else:
            age = int(age)
            score = int(score)
            edu = int(edu)
            if test == 'BFC':
                if age < 65 and edu <= 12:
                    df = self.benson_data[['Raw', 'Z score', 'Percentile', 'Classification']]
                elif age < 65 and edu > 12:
                    df = self.benson_data[['Raw', 'Z score2', 'Percentile2', 'Classification2']]
                elif age >= 65 and edu <= 12:
                    df = self.benson_data[['Raw', 'Z score3', 'Percentile3', 'Classification3']]
                else:
                    df = self.benson_data[['Raw', 'Z score4', 'Percentile4', 'Classification4']]
            elif test == 'BFR':
                if age < 65 and edu <= 12:
                    df = self.benson_recall_data[['Raw', 'Z score', 'Percentile', 'Classification']]
                elif age < 65 and edu > 12:
                    df = self.benson_recall_data[['Raw', 'Z score2', 'Percentile2', 'Classification2']]
                elif age >= 65 and edu <= 12:
                    df = self.benson_recall_data[['Raw', 'Z score3', 'Percentile3', 'Classification3']]
                else:
                    df = self.benson_recall_data[['Raw', 'Z score4', 'Percentile4', 'Classification4']]
            else:
                return '', '', ''
            df = df[df['Raw'] == score].reset_index(drop=True)
            raw, z_score, percent, classification = df.loc[0, :]
            if type(percent) == float:
                percent = round(percent, 1)
            return round(z_score, 2), percent, test+classification[0]
