import pandas as pd
import numpy as np


class CTT(object):
    def __init__(self):
        self.ctt1_data, self.ctt2_data = self.prepare_raw_data()

    @staticmethod
    def prepare_raw_data():
        df = pd.read_excel(r'C:\Users\wells\PycharmProjects\vgh_flask\data\常模總整理.xlsx', sheet_name='CTT')
        df1 = df[['校正後CTT1-時間', '百分等級']]
        df1 = df1[:241]
        df2 = df[['校正後CTT2-時間', '百分等級.1']]
        return df1, df2

    def measure(self, age=None, score=None, edu=None, gender=None, test=None):
        if score == '' or age == '' or gender == '' or test == '':
            return ''
        else:
            age = int(age)
            gender = int(gender)
            score = int(score)
            if test == 'CTT1-time':
                if gender == 1:
                    score_t = score + 3.682 - 1.71 * (age - 62.61) + 3.428 * (edu - 9.84)
                    percent = list(self.ctt1_data[self.ctt1_data['校正後CTT1-時間'] == score_t]['百分等級'])[0]
                elif gender == 2:
                    score_t = score - 3.682 - 1.71 * (age - 62.61) + 3.428 * (edu - 9.84)
                    percent = list(self.ctt1_data[self.ctt1_data['校正後CTT1-時間'] == score_t]['百分等級'])[0]
                else:
                    return ''
            elif test == 'CTT1-error':
                score_t = score + 0.007 * (edu - 9.84)
                if round(score_t, 0) == 0:
                    percent = '>16'
                elif round(score_t, 0) == 1:
                    percent = '2-4'
                else:
                    percent = '<=1'
            elif test == 'CTT1-approach-error':
                score_t = score + 0.003 * (age - 62.61)
                if round(score_t, 0) == 0:
                    percent = '>16'
                elif round(score_t, 0) == 1:
                    percent = '2-4'
                else:
                    percent = '<=1'
            elif test == 'CTT1-hint':
                score_t = score - 0.022 * (age - 62.61) + 0.032 * (edu - 9.84)
                if round(score_t, 0) == 0:
                    percent = '>16'
                elif round(score_t, 0) == 1:
                    percent = '7-16'
                elif round(score_t, 0) == 2:
                    percent = '2-4'
                else:
                    percent = '<=1'
            elif test == 'CTT2-time':
                if gender == 1:
                    score_t = score + 7.916 - 2.893 * (age - 62.61) + 5.576 * (edu - 9.84)
                    percent = list(self.ctt2_data[self.ctt2_data['校正後CTT2-時間'] == score_t]['百分等級.1'])[0]
                elif gender == 2:
                    score_t = score - 7.916 - 2.893 * (age - 62.61) + 5.576 * (edu - 9.84)
                    percent = list(self.ctt2_data[self.ctt2_data['校正後CTT2-時間'] == score_t]['百分等級.1'])[0]
                else:
                    return ''
            elif test == 'CTT2-color-error':
                score_t = score + 0.018 * (edu - 9.84)
                if round(score_t, 0) == 0:
                    percent = '>16'
                elif round(score_t, 0) == 1:
                    percent = '7-16'
                elif round(score_t, 0) == 2:
                    percent = '2-4'
                else:
                    percent = '<=1'
            elif test == 'CTT2-number-error':
                score_t = score + 0.013 * (edu - 9.84)
                if round(score_t, 0) == 0:
                    percent = '>16'
                elif round(score_t, 0) == 1:
                    percent = '2-4'
                else:
                    percent = '<=1'
            elif test == 'CTT2-approach-error':
                score_t = score
                if round(score_t, 0) == 0:
                    percent = '>16'
                elif round(score_t, 0) == 1:
                    percent = '2-4'
                else:
                    percent = '<=1'
            elif test == 'CTT2-hint':
                if gender == 1:
                    score_t = score-0.216-0.064*(age-62.61)+0.193*(edu-9.84)
                elif gender == 2:
                    score_t = score + 0.216 - 0.064 * (age - 62.61) + 0.193 * (edu - 9.84)
                else:
                    return ''
                if round(score_t, 0) < 4:
                    percent = '>16'
                elif round(score_t, 0) < 5:
                    percent = '7-16'
                elif round(score_t, 0) < 6:
                    percent = '5-6'
                elif round(score_t, 0) < 7:
                    percent = '2-4'
                else:
                    percent = '<=1'
            elif test == 'CTT-interference-index':
                score_t = score - 0.018*(edu-9.84)
                if round(score_t, 0) < 1.8:
                    percent = '>16'
                elif round(score_t, 0) < 2.2:
                    percent = '7-16'
                elif round(score_t, 0) < 2.4:
                    percent = '5-6'
                elif round(score_t, 0) < 2.7:
                    percent = '2-4'
                else:
                    percent = '<=1'
            else:
                return ''

            return percent
