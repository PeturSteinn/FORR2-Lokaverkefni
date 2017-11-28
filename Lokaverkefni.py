import random

class nagdyr:
    def __init__(self, nafn, tegund, stadsetning, afl):
        self.nafn = nafn
        self.teg = tegund
        self.stad = stadsetning
        self.afl = afl
    def upplysingar(self):
        return "Nafn: " + self.nafn + " | Tegund: " + self.teg + ' | Staðsetninging: ' + str(self.stad) + ' | Afl: ' + str(self.afl)



def action(nagdyr):
    global switchDirection
    switchDirection = False

    def checkIfCombat():
        if abs(mus.stad - rotta1.stad) <= 3: # Ef hún er nálægt rotta1
            print(mus.nafn + " er nálægt " + rotta1.nafn)
            if mus.afl < rotta1.afl:
                print(rotta1.nafn + " hendir músinni um " + str(rotta1.afl) + " reiti")
                mus.stad -= rotta1.afl
            elif mus.afl > rotta1.afl:
                print(mus.nafn + " sigrar " + rotta1.nafn + " því hún er með meira afl")

            else:
                print("Jafntefli á milli " + mus.nafn + " og " + rotta1.nafn)

        elif abs(mus.stad - rotta2.stad) <= 3:  # Ef hún er nálægt rotta2
            print(mus.nafn + " er nálægt " + rotta2.nafn)
            if mus.afl < rotta2.afl:
                print(rotta2.nafn + " hendir músinni um " + str(rotta2.afl) + " reiti")
                mus.stad -= rotta2.afl

            elif mus.afl > rotta2.afl:
                print(mus.nafn + " sigrar " + rotta2.nafn + " því hún er með meira afl")

            else:
                print("Jafntefli á milli " + mus.nafn + " og " + rotta2.nafn)
        elif abs(mus.stad - rotta3.stad) <= 3:   # Ef hún er nálægt rottu3
            print(mus.nafn + " er nálægt " + rotta3.nafn)
            if mus.afl < rotta3.afl:
                print(rotta3.nafn + " hendir músinni um " + str(rotta3.afl) + " reiti")
                mus.stad -= rotta3.afl

            elif mus.afl > rotta3.afl:
                print(mus.nafn + " sigrar " + rotta3.nafn + " því hún er með meira afl")

            else:
                print("Jafntefli á milli " + mus.nafn + " og " + rotta3.nafn)
    kast = random.randint(1, 6)
    if (nagdyr.teg == "mús"):
        for i in range(kast):
            print("Mús færir sig frá reit", nagdyr.stad, "yfir á reit ", end='')
            mus.stad += 1
            print(nagdyr.stad)
            checkIfCombat()

            if nagdyr.stad == hamstur.stad:
                print("Hamstur kastar mús um", hamstur.afl, "reiti")
                mus.stad += hamstur.afl
            elif nagdyr.stad == 100:
                break

    elif (nagdyr.teg == "rotta"):
        fiddy = random.randint(0,1)
        if fiddy == 0:
            kast = kast - 7
            print(nagdyr.nafn + " fer til vinstri um " + str(abs(kast)) + " reiti og er staðsett núna á " + str(nagdyr.stad))

            for i in range(abs(kast)):
                if nagdyr.stad <= 1 or switchDirection:
                    print(nagdyr.nafn + " færir sig frá reit", nagdyr.stad, "yfir á reit ", end='')
                    nagdyr.stad += 1
                    print(nagdyr.stad)
                    switchDirection = True

                else:
                    print(nagdyr.nafn + " færir sig frá reit", nagdyr.stad, "yfir á reit ", end='')
                    nagdyr.stad -= 1
                    print(nagdyr.stad)
                checkIfCombat()

        elif fiddy == 1:
            print(nagdyr.nafn + " fer til hægri um " + str(abs(kast)) + " reiti og er staðsett núna á " + str(nagdyr.stad))
            for i in range(kast):
                if nagdyr.stad >= 100 or switchDirection:
                    nagdyr.stad -= 1
                    switchDirection = True

                else:
                    print(nagdyr.nafn + " færir sig frá reit", nagdyr.stad, "yfir á reit ", end='')
                    nagdyr.stad += 1
                    print(nagdyr.stad)
                checkIfCombat()



    elif (nagdyr.teg == "hamstur"):
        for i in range(kast):
            if mus.stad < hamstur.stad:
                print("Hamstur færir sig frá reit", nagdyr.stad, "yfir á reit ", end='')
                hamstur.stad -= 1
                print(nagdyr.stad)
            elif mus.stad > hamstur.stad:
                print("Hamstur færir sig frá reit", nagdyr.stad, "yfir á reit ", end='')
                hamstur.stad += 1
                print(nagdyr.stad)
            elif mus.stad == hamstur.stad:
                print("Hamstur kastar mús um", nagdyr.afl, "reiti")
                mus.stad += hamstur.afl






kast = 0
fiddy = 0
switchDirection = False
mus = nagdyr('Mús','mús' , 1 , random.randrange(2,7,2))
rotta1 = nagdyr('Rotta1','rotta' , random.randrange(2,99) , random.randrange(2,7,2))
rotta2 = nagdyr('Rotta2','rotta' , random.randrange(2,99) , random.randrange(2,7,2))
rotta3 = nagdyr('Rotta3','rotta' , random.randrange(2,99) , random.randrange(2,7,2))
hamstur = nagdyr('Hamstur','hamstur' , random.randrange(2,99) , random.randrange(2,7,2))

print(mus.upplysingar())
print(rotta1.upplysingar())
print(rotta2.upplysingar())
print(rotta3.upplysingar())
print(hamstur.upplysingar())


print()
while True:
    action(mus)
    if (mus.stad >= 100):
        break
    print()
    action(rotta1)
    print()
    action(rotta2)
    print()
    action(rotta3)
    print()
    action(hamstur)
    print()
