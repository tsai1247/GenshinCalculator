from Database.FullInformation import FullInformation
from File import File

def main():
    data = File.Read()
    characterdata = FullInformation(data)
    File.Write(characterdata.detail)

if __name__ == '__main__':
    main()

