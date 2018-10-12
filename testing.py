import sys
sys.path.insert(0, './lib')
import files

with open("ignoregit/trackblock00.sav", "rb") as binary_file:
    data = files.HeroPath(binary_file)
    storage = 0
    storage2 = 0
    storage3 = ""
    print(data.sections[0][4].hex())
