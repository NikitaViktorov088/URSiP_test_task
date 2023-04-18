import pandas as pd
from sqlalchemy import text


class DataReader:
    def __init__(self, filepath, db):
        self.filepath = filepath
        self.db = db
        self.columns = ['id', 'company', 'Qliq_fact_d1',
                        'Qliq_fact_d2', 'Qoil_fact_d1',
                        'Qoil_fact_d2', 'Qliq_fore_d1',
                        'Qliq_fore_d2', 'Qoil_fore_d1', 'Qoil_fore_d2'
                        ]

    def read_data(self):
        df = pd.read_excel(self.filepath, skiprows=2, names=self.columns)
        df['date'] = pd.date_range(start='2023-03-01', end='2023-03-20')
        self.db.save_data(df)


class DataProcessor:
    def __init__(self, db):
        self.db = db

    def get_result(self):
        stmt = text('''SELECT *,
        (Qliq_fact_d1 + Qliq_fact_d2) AS TOTAL_LIQ_FACT,
        (Qoil_fact_d1 + Qoil_fact_d2) AS TOTAL_OIL_FACT,
        (Qliq_fact_d1 + Qliq_fact_d2) AS TOTAL_LIQ_FORE,
        (Qoil_fore_d1 + Qoil_fore_d2) AS TOTAL_OIL_FORE
        FROM companies
        GROUP BY date''')
        df_result = pd.read_sql_query(stmt, self.db.con)
        self.db.save_result(df_result)
