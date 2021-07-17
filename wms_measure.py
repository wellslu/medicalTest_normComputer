import pandas as pd
import numpy as np

class WMN(object):
    def __init__(self):
        self.wms_data = self.prepare_raw_data()

    @staticmethod
    def prepare_raw_data():
        df = pd.read_excel('data/常模總整理.xlsx', sheet_name='衛氏')
        df.columns = [i for i in range(len(df.columns))]
        result = pd.DataFrame()
        for i in range(3, 52, 5):
            df_t = df[[0, 1, 2] + [i for i in range(i, i + 5)]]
            age = df_t.loc[0, i]
            df_t.columns = df_t.loc[1, :]
            df_t = df_t[2:21].reset_index(drop=True)
            df_t.loc[:, 'age'] = age.split('-')[0]
            for col in df_t.columns[3:]:
                df_t[col] = df_t[col].astype('str')
            df_t['LM-1'] = df_t['LM-1'].apply(lambda x: x.split('-')[0] if '-' in x else x)
            df_t['LM-2'] = df_t['LM-2'].apply(lambda x: x.split('-')[0] if '-' in x else x)
            df_t['DSF'] = df_t['DSF'].apply(lambda x: x.split('-')[0] if '-' in x else x)
            df_t['DSB'] = df_t['DSB'].apply(lambda x: x.split('-')[0] if '-' in x else x)
            df_t['符號替代'] = df_t['符號替代'].apply(lambda x: x.split('-')[0] if '-' in x else x)
            for col in df_t.columns[3:]:
                df_t[col] = df_t[col].replace('—', 999).astype('int')
            df_t = df_t.replace(999, np.nan)
            result = pd.concat([result, df_t], ignore_index=True)
        result = result.sort_values(['age', '量表分數']).reset_index(drop=True)
        return result

    def measure(self, age=None, score=None, test=None):
        if score == '' or age == '' or test == '':
            return '', '', ''
        else:
            age = int(age)
            score = int(score)
            df = self.wms_data[self.wms_data['age']<=age].loc[self.wms_data[test]<=score]
            z_score = list(df['Z score'])[-1]
            percent = list(df['百分位數'])[-1]
            table_score = list(df['量表分數'])[-1]
            if type(percent) == float:
                percent = round(percent, 1)
            return round(z_score, 2), percent, table_score