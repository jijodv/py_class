class film():
    def __init__(self, fname, fgenre):
        self.fname = fname
        self.fgenre = fgenre
    def say(self):
        print "Film {} is of genre {}" .format(self.fname, self.fgenre)

hfilm = film("Aval", "Horror")

hfilm.say()
