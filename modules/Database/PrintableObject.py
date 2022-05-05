import json
from typing import Dict

class PrintableObject():
    def ToString(self) -> str:
        return json.dumps(self, default=vars, indent=4)

    def ToJSON(self) -> Dict:
        return json.loads(self.ToString())

    def Print(self) -> None:
        print(self.ToString())
