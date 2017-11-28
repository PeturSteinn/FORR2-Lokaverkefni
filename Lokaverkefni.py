import random

class nagdyr:
    def __init__(self , tegund , stadsetning , afl):
        self.teg = tegund
        self.stad = stadsetning
        self.afl = afl
    def upplysingar(self):
        return "ég er "+ self.teg + " aflið er " + str(self.afl) + ' staðsetninging ' + str(self.stad)



mus = nagdyr('mús' , 1 , random.randrange(2,7,2))
rotta1 = nagdyr('rotta1' , random.randrange(2,99) , random.randrange(2,7,2))
rotta2 = nagdyr('rotta2' , random.randrange(2,99) , random.randrange(2,7,2))
rotta3 = nagdyr('rotta3' , random.randrange(2,99) , random.randrange(2,7,2))
hamstur = nagdyr('hamstur' , random.randrange(2,99) , random.randrange(2,7,2))

print(mus.upplysingar())
print(rotta1.upplysingar())
print(rotta2.upplysingar())
print(rotta3.upplysingar())
print(hamstur.upplysingar())