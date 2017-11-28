import random

class nagdyr:
    def __init__(self , tegund , stadsetning , afl):
        self.teg = tegund
        self.stad = stadsetning
        self.afl = afl
    def upplysingar(self):
        return "ég er "+ self.teg + " aflið er " + str(self.afl) + ' staðsetninging ' + str(self.stad)



def labb(nagdyr):
    kast = random.randint(1, 6)
    #print(mus.stad, "BEFORE")
    if (nagdyr.teg == "mús"):
        mus.stad += kast
        #print(mus.stad, "AFTER")

    elif (nagdyr.teg == "rotta"):
        fiddy = random.randint(0,1)
        #print(fiddy, "AFRAM EÐA AFTURABAK")
        if fiddy == 0:
            #print(kast, "BEFORE")
            kast = kast - 7
            #print(kast, "AFTER")
            nagdyr.stad += kast


        elif fiddy == 1:
            #print(kast, "BEFORE")
            #print(kast, "AFTER")
            nagdyr.stad += kast

    elif (nagdyr.teg == "hamstur"):
        for i in range(kast):
            if mus.stad < hamstur.stad:
                print("Hamstur færir sig niður")
                hamstur.stad -= 1
            elif mus.stad > hamstur.stad:
                print("Hamstur færir sig upp")
                hamstur.stad += 1
            elif mus.stad == hamstur.stad:
                print("Hamstur kastar mús")
                mus.stad += hamstur.afl






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
#labb(rotta1)
#labb(rotta2)
#labb(rotta3)
while(mus.stad < 100):
    print(mus.stad, "Mús staðsetning BEFORE")
    labb(mus)
    print(mus.stad, "Mús staðsetning AFTER")
    print(hamstur.stad, "Hamstur staðsetning BEFORE")
    labb(hamstur)
    print(hamstur.stad, "Hamstur staðsetning AFTER")

#print(kast, "AFTER")
#print(mus.stad, "AFTER")
