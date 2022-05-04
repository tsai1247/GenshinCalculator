import sqlite3
from typing import Dict, List
from Database.Attributes import Attributes
from Database.PrintableObject import PrintableObject

class Stat(PrintableObject):
    def __init__(self, data: Dict):
        self.Name = None
        self.Value = None

        if 'Value' in data.keys():
            self.init2Val(data["Name"], data["Value"])
        elif 'Name' in data.keys():
            self.init1Val(data["Name"])

    def init2Val(self, Name, Value) -> None:
        self.Name = Name
        self.Value = Value
    
    def init1Val(self, Name) -> None:
        self.Name = Name

        sql = sqlite3.connect('Data.db')
        cursor = sql.cursor()
        cursor.execute('SELECT MaxVal FROM SecondaryStat WHERE Name = ?', [self.Name])
        ret = cursor.fetchall()
        if len(ret) == 0:
            self.Value: float = None
        else:
            self.Value: float = ret[0][0]
        cursor.close()
        sql.close()

    def ToAttribute(self) -> Attributes:
        ret = Attributes()
        ret.Add({
            self.Name: self.Value
        })
        return ret

class Artifact(PrintableObject):
    def __init__(self, data: Dict) -> None:
        self.Kind: int = data["Kind"]   # Name of Each Artifact Set
        self.Type: int = data["Type"]   # Flower of Life, Plume of Death, Sands of Eon, Goblet of Eonothem, Circlet of Logos
        self.Level: int = data["Level"]
        self.MainStat = Stat(data["MainStat"])
        self.SubStats = [ Stat(i) for i in data["SubStat"] ]
    
    def ToAttribute(self) -> Attributes:
        ret = Attributes()
        ret += self.MainStat.ToAttribute()
        for substat in self.SubStats:
            ret += substat.ToAttribute()
        return ret

class ArtifactSet(PrintableObject):
    def __init__(self, data: Dict) -> None:
        self.artifacts: List[Artifact] = [Artifact(artifactData) for artifactData in data]
    
    @property
    def Flower_of_Life(self):
        return self.artifacts[0]
    @property
    def Plume_of_Death(self):
        return self.artifacts[1]
    @property
    def Sands_of_Eon(self):
        return self.artifacts[2]
    @property
    def Goblet_of_Eonothem(self):
        return self.artifacts[3]
    @property
    def Circlet_of_Logos(self):
        return self.artifacts[4]
    
    def ToAttribute(self) -> Attributes:
        ret = Attributes()
        for artifact in self.artifacts:
            ret += artifact.ToAttribute()
        return ret
