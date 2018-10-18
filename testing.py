import sys
sys.path.insert(0, './lib')
import files
from PIL import Image, ImageDraw

img = Image.new('RGB', (1000,800), color = 'red')

with open("ignoregit/trackblockAA.sav", "rb") as binary_file:
    data = files.HeroPath(binary_file, 'little')
    section1coords = []
    sectionno = 0
    for h in data.sections:
        img = Image.new('RGBA', (1000,800), color=(255,255,255,0))
        for s in h:
            f = []
            f.append(s.flag)
            f.append(s.x)
            f.append(s.y)
            if(int(s.y / 10) + 400 == 370):
                print(h)
            section1coords.append(f)
            if(int(s.x / 10) + 500 > 1000 or int(s.x / 10) + 500 < 0):
                continue
            if(int(s.y / 10) + 400 > 800 or int(s.y / 10) + 400 < 0):
                continue

            img.putpixel((int(s.x / 10) + 500,int(s.y / 10) + 400), (2,173,219))
        img.save('ignoregit/blockAA.{}.png'.format(sectionno))
        sectionno += 1
print('ready')

with open("ignoregit/trackblockAA.dat", 'w') as out_file:
    for item in section1coords:
        out_file.write("%s\n" % item)
    out_file.close()
