import json
from Database.Artifact import ArtifactSet
from Database.Character import Character
from Database.Attributes import Attributes, AttributesDetail
from Database.PrintableObject import PrintableObject
from Database.Weapon import Weapon

class FullInformation(PrintableObject):
    def __init__(self, data) -> None:
        if isinstance(data, str):
            data = json.loads(data)
        
        self.character = Character(data["Character"])
        self.weapon = Weapon(data["Weapon"])
        self.artifactSet = ArtifactSet(data["Artifact"])
        
    @property
    def attributes(self):
        ret = Attributes.Default()
        ret += self.character.ToAttribute()
        ret += self.weapon.ToAttribute()
        ret += self.artifactSet.ToAttribute()
        return ret

    @property
    def detail(self, Beta = False):
        return AttributesDetail(self.attributes, Beta=Beta)
