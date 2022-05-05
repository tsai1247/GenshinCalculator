import math
from typing import Dict
from typing_extensions import Self
from Database.PrintableObject import PrintableObject
import numbers

class Attributes(PrintableObject):
    @classmethod
    def Default(self) -> Self:
        ret = Attributes()
        ret.Max_Stamina = 240
        ret.Crit_Rate = 5
        ret.Crit_Dmg = 50
        ret.Energy_Recharge = 100
        return ret

    def __init__(self) -> None:
        self.BaseHp = 0.0
        self.BaseAtk = 0.0
        self.BaseDef = 0.0
        self.Hp = 0.0   # AdditionalHp
        self.Atk = 0.0  # AdditionalAtk
        self.Def = 0.0  # AdditionalDef
        self.Hp_Percent = 0.0
        self.Atk_Percent = 0.0
        self.Def_Percent = 0.0
        self.Elemental_Mastery = 0.0
        self.Max_Stamina = 0.0
        self.Crit_Rate = 0.0
        self.Crit_Dmg = 0.0
        self.Healing_Bonus = 0.0
        self.Incoming_Healing_Bonus = 0.0
        self.Energy_Recharge = 0.0
        self.CD_Reduction = 0.0
        self.Shield_Strength = 0.0
        
        self.Pyro_Dmg = 0.0
        self.Pyro_Res = 0.0
        
        self.Hydro_Dmg = 0.0
        self.Hydro_Res = 0.0
        
        self.Dendro_Dmg = 0.0
        self.Dendro_Res = 0.0
        
        self.Electro_Dmg = 0.0
        self.Electro_Res = 0.0
        
        self.Anemo_Dmg = 0.0
        self.Anemo_Res = 0.0
        
        self.Cryo_Dmg = 0.0
        self.Cryo_Res = 0.0
        
        self.Geo_Dmg = 0.0
        self.Geo_Res = 0.0
        
        self.Physical_Dmg = 0.0
        self.Physical_Res = 0.0

    def __add__(self, o: Self) -> Self:
        for attribute in dir(self):
            if eval(f'isinstance(self.{attribute}, numbers.Number)'):
                exec(f'self.{attribute} += o.{attribute}')
        return self
    
    def Add(self, data: Dict):
        for key in data.keys():
            exec(f'self.{key} += {data[key]}')

class AttributesDetail(PrintableObject):
    def __init__(self, attributes: Attributes, Beta = False) -> None:
        if not Beta:
            self.Hp = math.floor(attributes.BaseHp) + math.floor(attributes.BaseHp * attributes.Hp_Percent/100) + math.floor(attributes.Hp)
            self.Atk = math.floor(attributes.BaseAtk) + math.floor(attributes.BaseAtk * attributes.Atk_Percent/100) + math.floor(attributes.Atk)
            self.Def = math.floor(attributes.BaseDef) + math.floor(attributes.BaseDef * attributes.Def_Percent/100) + math.floor(attributes.Def)
            
            self.Elemental_Mastery = round(attributes.Elemental_Mastery)
            
            for i in attributes.__dict__.keys():
                if 'Hp' not in i and 'Atk' not in i and 'Def' not in i and 'Elemental_Mastery' not in i:
                    exec(f'self.{i} = round(attributes.{i}, 1)')
        else:
            self.Hp = math.floor(attributes.BaseHp + attributes.BaseHp * attributes.Hp_Percent/100 + attributes.Hp)
            self.Atk = math.floor(attributes.BaseAtk + attributes.BaseAtk * attributes.Atk_Percent/100 + attributes.Atk)
            self.Def = math.floor(attributes.BaseDef + attributes.BaseDef * attributes.Def_Percent/100 + attributes.Def)

            self.Elemental_Mastery = round(attributes.Elemental_Mastery)
            
            for i in attributes.__dict__.keys():
                if 'Hp' not in i and 'Atk' not in i and 'Def' not in i and 'Elemental_Mastery' not in i:
                    exec(f'self.{i} = round(attributes.{i}, 1)')