from parser.parser import DataProcessor, DataReader

from core.db import DataBase

if __name__ == '__main__':
    db = DataBase()
    reader = DataReader('file_data.xlsx', db)
    reader.read_data()
    processor = DataProcessor(db)
    processor.get_result()
