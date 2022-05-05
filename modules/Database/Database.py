from abc import abstractmethod
import sqlite3
from typing import Dict
from Database.Attributes import Attributes
from Database.PrintableObject import PrintableObject

class Database(PrintableObject):
    def __init__(self, data: Dict) -> None:
        self.Name = data["Name"]
        self.Level = data["Level"]
        self.SetVariables()

    @property
    def data(self):
        Level = 90 # lock the level
        ret = [Level]
        sql = sqlite3.connect('Data.db')
        cursor = sql.cursor()
        cursor.execute(f'SELECT * FROM {self.__class__.__name__} WHERE Name = ?', [self.Name])
        data = cursor.fetchall()
        if len(data) == 0:
            ret = None
        else:
            ret += data[0]
        cursor.close()
        sql.close()
        
        if ret:
            return ret
        else:
            raise Exception(f'{self.__class__.__name__} named "{self.Name}" is not found.')

    @abstractmethod
    def SetVariables(self):
        pass

    @abstractmethod
    def ToAttribute(self) -> Attributes:
        pass
