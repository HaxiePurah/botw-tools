from bitstring import BitStream
class Section:
    def __init__(self, data):
        if(data != None):
            self._data = BitStream(hex=data.hex())
        else:
            self._data = None
        self.x = self._read_x()
        self.y = self._read_y()
        self.flag = self._read_flag()
        self.vector = []
        self.vector.append(self.x)
        self.vector.append(self.y)
    def _read_x(self):
        self._data.pos = 6
        return self._data.read('int:13')
        return None
    def _read_y(self):
        self._data.pos = 19
        return self._data.read('int:13')
        return None
    def _read_flag(self):
        self._data.pos = 0
        return self._data.read('uint:6')
        return None

class Segment:
    def __init__(self, data):
        self.header = self._read_header()
        self.sections = self._read_sections()

class HeroPath:
    def __init__(self, file, byteorder):
        self._file = file
        self._byteorder = byteorder
        self.header = self._read_header()
        self.segments = self._read_segments()
        self.sections = self._read_sections()
    def _read_header(self):
        self._file.seek(0, 0)
        return self._file.read(64)
        # TODO: RE Header system, re-work this to return more than just bytes)
    def _read_segments(self):
        segments = [0 for i in range(53)]
        for segno in range(53):
            segments[segno] = self._read_segment(segno)
        return segments
    def _read_segment(self, segno):
        startpos = (1216 * segno) + 64
        self._file.seek(startpos, 0)
        if(int.from_bytes(self._file.read(4), byteorder=self._byteorder) == 0):
            return None
        self._file.seek(startpos, 0)
        return self._file.read(1216)
    def _read_sections(self):
        sections = [[0 for i in range(303)] for j in range(53)]
        for segno in range(53):
            for secno in range(303):
                sections[segno][secno] = self._read_section(segno, secno)
        return sections
    def _read_section(self, segno, secno):
        startpos = (1216 * segno) + 64
        self._file.seek(startpos, 0)
        self._file.seek(secno * 4, 1)
        return Section(self._file.read(4))
