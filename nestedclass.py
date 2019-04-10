# class parent
#2 attributes
#2 methods

# class child
# 1 attributes
# 1 methods

class Par():
    def __init__(self, name, comp):
        self.name = name
        self.comp = comp
    def par_meth(self):
        print ("{} works at {}" .format(self.name, self.comp))

class Chi(Par):
    def __init__(self, name, comp, dom):
        self.dom = dom
        super().__init__(name, comp)
    def chi_meth(self):
        print ("{} works at {} in {} domain" .format(self.name, self.comp, self.dom))


bpar = Par("balaji", "DB")
bchi = Chi("balaji", "DB", "UNIX")
