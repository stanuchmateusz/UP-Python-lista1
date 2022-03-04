class Telewizor:
    def __init__(self,):
        self._nrKanalu = None
        self._poziomGlosnosci = None

    @property
    def kanal(self) -> int:
        return self._nrKanalu

    @kanal.setter
    def kanal(self, nrKanalu):
        if nrKanalu < 1:
            self._nrKanalu = 1
        elif nrKanalu > 999:
            self._nrKanalu = 999
        else:
            self._nrKanalu = nrKanalu

    @property
    def glosnosc(self) -> int:
        return self._poziomGlosnosci

    @glosnosc.setter
    def glosnosc(self, poziomGlosnosci):
        if poziomGlosnosci < 0:
            self._poziomGlosnosci = 0
        elif poziomGlosnosci > 10:
            self._poziomGlosnosci = 10
        else:
            self._poziomGlosnosci = poziomGlosnosci


if __name__ == '__main__':
    telewizor = Telewizor()
    telewizor.kanal = 454545
    telewizor.glosnosc = -34
    print("""
                    o
           o       /
            \     /
             \   /
              \ /
+--------------v-------------+
|  __________________      @ |
| /                  \       |
| |             ,--, |  (\)  |
| |       _ ___/ /\| |       |
| |   ,;`( )__, )  ~ |  (-)  |
| |  // o//   '--;   |       |
| \  ' o \     |     / :|||: |
|  -ooo--------------  :|||: |
+----------------------------+
   []                    []
    """)
    print(telewizor.kanal)
    print(telewizor.glosnosc)
