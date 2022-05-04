from datetime import datetime
import json

from Database.PrintableObject import PrintableObject

class File:
    @staticmethod
    def Read(path = 'in.json'):
        fr = open(path, 'r')
        ret = ''.join(fr.readlines())
        fr.close()
        return ret
    
    @staticmethod
    def Write(data: PrintableObject, path = 'out.json'):
        data = data.ToJSON()
        curTime = datetime.now().strftime('%Y/%m/%d, %H:%M:%S')
        data = {'timestamp': curTime, 'Attributes': data}
        data = json.dumps(data, indent=4)

        fw = open(path, 'w')
        fw.write(data)
        fw.close()