import pandas as pd
import numpy as np


class Clock_Drawing(object):
    def __init__(self):
        self.clock_drawing_data = self.prepare_raw_data()

    @staticmethod
    def prepare_raw_data():
        df = pd.read_excel(r'C:\Users\wells\PycharmProjects\vgh_flask\data\常模總整理.xlsx', sheet_name='畫鐘')
        df.columns = df.loc[3, :]
        df = df[4:15]
        return df

    def measure(self, age=None, score=None, edu=None):
        if edu == '' or score == '' or age == '':
            return '', '', ''
        else:
            age = int(age)
            if age < 55 or age > 98:
                return '', '', ''
            score = int(score)
            edu = int(edu)
            if age <= 74 and edu <= 12:
                df = self.clock_drawing_data[['Raw', 'Z score', 'Percentile', 'Classification']]
            elif age <= 74 and edu > 12:
                df = self.clock_drawing_data[['Raw', 'Z score2', 'Percentile2', 'Classification2']]
            elif age >= 75 and edu <= 12:
                df = self.clock_drawing_data[['Raw', 'Z score3', 'Percentile3', 'Classification3']]
            else:
                df = self.clock_drawing_data[['Raw', 'Z score4', 'Percentile4', 'Classification4']]
            df = df[df['Raw'] == score].reset_index(drop=True)
            raw, z_score, percent, classification = df.loc[0, :]
            if type(percent) == float:
                percent = round(percent, 1)
            return round(z_score, 2), percent, 'CDT'+classification[0]