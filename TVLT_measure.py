import pandas as pd
import numpy as np


class TVLT(object):
    def __init__(self):
        self.tvlt_data, self.tvlt_recall_data = self.prepare_raw_data()

    @staticmethod
    def prepare_raw_data():
        df = pd.read_excel(r'C:\Users\wells\PycharmProjects\vgh_flask\data\常模總整理.xlsx', sheet_name='TVLT全')
        df1 = df[3:]
        df1.columns = df.loc[2, :]
        df1 = df1[['Raw', 'Z score', 'Percentile', 'Classification', 'Z score2', 'Percentile2', 'Classification2']]
        df2 = df[21:]
        df2.columns = df.loc[20, :]
        df2 = df2[['Raw', 'Z score', 'Percentile', 'Classification', 'Z score2', 'Percentile2', 'Classification2',
                   'Z score3', 'Percentile3', 'Classification3', 'Z score4', 'Percentile4', 'Classification4']]
        return df1, df2

    def measure(self, age=None, score=None, test=None):
        if score == '' or age == '':
            return '', '', ''
        else:
            age = int(age)
            if age < 60 or age > 84:
                return '', '', ''
            score = int(score)
            if test == 'TVLTIR':
                if age < 72:
                    df = self.tvlt_data[['Raw', 'Z score', 'Percentile', 'Classification']]
                else:
                    df = self.tvlt_data[['Raw', 'Z score2', 'Percentile2', 'Classification2']]
            elif test == 'TVLTDR':
                if age < 72:
                    df = self.tvlt_recall_data[['Raw', 'Z score', 'Percentile', 'Classification']]
                else:
                    df = self.tvlt_recall_data[['Raw', 'Z score2', 'Percentile2', 'Classification2']]
            elif test == 'TVLTDI':
                if age < 72:
                    df = self.tvlt_recall_data[['Raw', 'Z score3', 'Percentile3', 'Classification3']]
                else:
                    df = self.tvlt_recall_data[['Raw', 'Z score4', 'Percentile4', 'Classification4']]
            else:
                return '', '', ''
            df = df[df['Raw'] == score].reset_index(drop=True)
            raw, z_score, percent, classification = df.loc[0, :]
            if type(percent) == float:
                percent = round(percent, 1)
            return round(z_score, 2), percent, test + classification[0]
