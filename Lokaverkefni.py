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
    kast = random.randint(1, 6)
    if (nagdyr.teg == "mús"):
        for i in range(kast):
            print("Mús færir sig frá reit", nagdyr.stad, "yfir á reit ", end='')
            mus.stad += 1
            print(nagdyr.stad)
            if abs(nagdyr.stad - rotta1.stad) <= 3:
                print(nagdyr.nafn + " er nálægt " + rotta1.nafn)
            elif abs(nagdyr.stad - rotta2.stad) <= 3:
                print(nagdyr.nafn + " er nálægt " + rotta2.nafn)
            elif abs(nagdyr.stad - rotta3.stad) <= 3:
                print(nagdyr.nafn + " er nálægt " + rotta3.nafn)

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
                    print(nagdyr.nafn + " Switched direction -----------------------")
                    if abs(nagdyr.stad - mus.stad) <= 3:
                        print(nagdyr.nafn + " er nálægt músinni!")

                    switchDirection = True

                else:
                    print(nagdyr.nafn + " færir sig frá reit", nagdyr.stad, "yfir á reit ", end='')
                    nagdyr.stad -= 1
                    print(nagdyr.stad)
                    if abs(nagdyr.stad - mus.stad) <= 3:
                        print(nagdyr.nafn + " er nálægt músinni!")





        elif fiddy == 1:
            print(nagdyr.nafn + " fer til hægri um " + str(abs(kast)) + " reiti og er staðsett núna á " + str(nagdyr.stad))
            for i in range(kast):
                if nagdyr.stad >= 100 or switchDirection:
                    nagdyr.stad -= 1
                    print(nagdyr.nafn + " Switched direction -----------------------")
                    if abs(nagdyr.stad - mus.stad) <= 3:
                        print(nagdyr.nafn + " er nálægt músinni!")

                    switchDirection = True

                else:
                    print(nagdyr.nafn + " færir sig frá reit", nagdyr.stad, "yfir á reit ", end='')
                    nagdyr.stad += 1
                    print(nagdyr.stad)
                    if abs(nagdyr.stad - mus.stad) <= 3:
                        print(nagdyr.nafn + " er nálægt músinni!")


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
