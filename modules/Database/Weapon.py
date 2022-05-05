from Database.Attributes import Attributes
from Database.Database import Database


class Weapon(Database):
    # [Level, Name, Star, Type, FullAtk, SecondaryStat, BaseSecondaryStatVal]
    def SetVariables(self):
        data = self.data
        self.Name = data[1]
        self.Star = data[2]
        self.Type = data[3]
        self.FullAtk = data[4]
        self.SecondaryStat = data[5]
        self.FullSecondaryStatVal = data[6]
        self.Atk = self._Atk
        self.SecondaryStatVal = self._SecondaryStatVal

    @property
    def _Atk(self):
        return self.FullAtk

    @property
    def _SecondaryStatVal(self):
        return self.FullSecondaryStatVal

    def ToAttribute(self) -> Attributes:
        ret = Attributes()
        ret.Add({
            "BaseAtk": self.Atk,
            self.SecondaryStat: self.SecondaryStatVal
        })

        return ret