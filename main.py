from core.db import DataBase
from parser.parser import DataReader, DataProcessor


if __name__ == '__main__':
    db = DataBase()
    reader = DataReader('file_data.xlsx', db)
    reader.read_data()
    processor = DataProcessor(db)
    processor.get_result()