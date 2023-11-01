class Cabeça:
    def __init__(self):
        pass

class Boneco:
    def __init__(self):
        self.cabeça = Cabeça()

    def __del__(self):
        del self.cabeça

boneco1 = Boneco() 
del boneco1
