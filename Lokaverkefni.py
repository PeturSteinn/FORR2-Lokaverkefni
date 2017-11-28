import random

class nagdyr:
    def __init__(self , tegund , stadsetning , afl):
        self.teg = tegund
        self.stad = stadsetning
        self.afl = afl
    def upplysingar(self):
        return "ég er "+ self.teg + " aflið er " + str(self.afl) + ' staðsetninging ' + str(self.stad)



def labb(tegund):
    kast = random.randint(1, 6)
    #print(mus.stad, "BEFORE")
    if (tegund == "mús"):
        mus.stad += kast
        print(mus.stad, "AFTER")

    elif (tegund == "rotta"):
        fiddy = random.randint(0,1)
        kast = random.randint(1,6)
        print(fiddy, "AFRAM EÐA AFTURABAK")
        if fiddy == 0:
            print(kast, "BEFORE")
            kast = kast - 7
            print(kast, "AFTER")
            return kast
        elif fiddy == 1:
            print(kast, "BEFORE")
            print(kast, "AFTER")
            return kast






kast = 0
fiddy = 0
mus = nagdyr('mús' , 1 , random.randrange(2,7,2))
rotta1 = nagdyr('rotta' , random.randrange(2,99) , random.randrange(2,7,2))
rotta2 = nagdyr('rotta' , random.randrange(2,99) , random.randrange(2,7,2))
rotta3 = nagdyr('rotta' , random.randrange(2,99) , random.randrange(2,7,2))
hamstur = nagdyr('hamstur' , random.randrange(2,99) , random.randrange(2,7,2))

print(mus.upplysingar())
print(rotta1.upplysingar())
print(rotta2.upplysingar())
print(rotta3.upplysingar())
print(hamstur.upplysingar())

#while(mus.stad != 100):
#print(mus.stad, "BEFORE")
#print(kast, "BEFORE")

print()
#mus.stad += kast
#labb(mus.teg)
labb(rotta1.teg)
labb(rotta2.teg)
labb(rotta3.teg)
#print(kast, "AFTER")
#print(mus.stad, "AFTER")
