import sqlite3
from Database.Attributes import Attributes
from Database.Database import Database

class Character(Database):
    # [Level, Name, Star, Vision, FullHp, FullAtk, FullDef, SecondaryStat]
    def SetVariables(self):
        data = self.data
        self.Name = data[1]
        self.Star = data[2]
        self.Vision = data[3]
        self.FullHp = data[4]
        self.FullAtk = data[5]
        self.FullDef = data[6]
        self.SecondaryStat = data[7]
        self.Hp = self._Hp
        self.Atk = self._Atk
        self.Def = self._Def
        self.SecondaryStatVal = self._SecondaryStatVal
    
    @property
    def _Hp(self):
        return self.FullHp
        
    @property
    def _Atk(self):
        return self.FullAtk
        
    @property
    def _Def(self):
        return self.FullDef

    @property
    def _SecondaryStatVal(self):
        sql = sqlite3.connect('Data.db')
        cursor = sql.cursor()
        cursor.execute('SELECT BaseVal FROM SecondaryStat WHERE Name = ?', [self.SecondaryStat])
        ret = cursor.fetchall()
        cursor.close()
        sql.close()
        if len(ret) == 0:
            baseVal = None
        else:
            baseVal = ret[0][0] * (4.94 if self.Star == 5 else 4.12)
            Level = self.Level
            if Level <= 40:
                baseVal *= 0
            elif Level <= 50:
                baseVal *= 0.25
            elif Level <= 70:
                baseVal *= 0.5
            elif Level <= 80:
                baseVal *= 0.75
            elif Level <= 90:
                baseVal *= 1
        if 'Elemental_Mastery' == self.SecondaryStat:
            return round(baseVal)
        else:
            return round(baseVal, 1)

    def ToAttribute(self) -> Attributes:
        ret = Attributes()
        ret.Add({
            "BaseHp": self.Hp,
            "BaseAtk": self.Atk,
            "BaseDef": self.Def,
            self.SecondaryStat: self.SecondaryStatVal
        })

        return ret