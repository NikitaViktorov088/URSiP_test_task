from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    company = Column(String)
    date = Column(DateTime)
    Qliq_fact_d1 = Column(Integer)
    Qliq_fact_d2 = Column(Integer)
    Qoil_fact_d1 = Column(Integer)
    Qoil_fact_d2 = Column(Integer)
    Qliq_fore_d1 = Column(Integer)
    Qliq_fore_d2 = Column(Integer)
    Qoil_fore_d1 = Column(Integer)
    Qoil_fore_d2 = Column(Integer)

class DataBase:
    def __init__(self):
        self.engine = create_engine('sqlite:///mydatabase.db', echo=True)
        Base.metadata.create_all(self.engine)
        self.con = self.engine.connect()
    
    def save_data(self, df):
        df.to_sql('companies', self.con, if_exists='replace', index=False)

    def save_result(self, df):
        df.to_excel('result.xlsx', index=False)
