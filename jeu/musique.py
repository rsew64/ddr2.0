import time

class Musique:
    def __init__ (self):
        self.playtime = 0
        self.musicduration = 10
        self.ok = 0

    def timecalc (self):
        while self.playtime<self.musicduration:
            self.ok = 1
            self.playtime += 1
            time.sleep(1)
        self.ok = 0

