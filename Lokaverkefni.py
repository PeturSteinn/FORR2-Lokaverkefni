import random

class nagdyr:   # Nagdýr búið til og gefið nafn, tegund, staðsetningu, afl
    def __init__(self, nafn, tegund, stadsetning, afl):
        self.nafn = nafn
        self.teg = tegund
        self.stad = stadsetning
        self.afl = afl
    def upplysingar(self):  # Hægt að nota þetta def til að prenta út stats á nagdýrunum
        return "Nafn: " + self.nafn + " | Tegund: " + self.teg + ' | Staðsetninging: ' + str(self.stad) + ' | Afl: ' + str(self.afl)

def drawPos():
    reitir_allt = str()
    reitir_nafn = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    reitir_map = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
    reitir_end_mark = ['                                                                                                   |']
    reitir_end = ['                                                                                                  END']
    reitir_map[mus.stad - 1] = "^"
    reitir_nafn[mus.stad - 1] = "M"
    reitir_map[rotta1.stad - 1] = "*"
    reitir_nafn[rotta1.stad - 1] = "R"
    reitir_map[rotta2.stad - 1] = "*"
    reitir_nafn[rotta2.stad - 1] = "R"
    reitir_map[rotta3.stad - 1] = "*"
    reitir_nafn[rotta3.stad - 1] = "R"
    reitir_map[hamstur.stad - 1] = "O"
    reitir_nafn[hamstur.stad - 1] = "H"
    for i in reitir_nafn:
        print(i, end='')
    print()
    for i in reitir_map:
        print(i, end='')
    print()
    for i in reitir_end_mark:
        print(i, end='')
    print()
    for i in reitir_end:
        print(i, end='')
    print()


def action(nagdyr): # Þessi def tekur við hvaða nagdýri sem er og keyrir það á viðeigandi hátt
    global switchDirection  # Hægt er að nota þessa bool núna hvar sem er.
    global counter
    switchDirection = False # Þessi boolean breyta er til að sjá til þess að rotturnar klessa ekki á vegg og snúa þeim við þegar þær gera það og meir að segja láta þær halda áfram með skrefin sem þau eiga eftir.
    def checkIfCombat():    # Þessi def athugar hvort rottur séu nálægt mús og keyrir á viðeigandi hátt.
        if abs(mus.stad - rotta1.stad) <= 3: # Ef músin er nálægt rotta1 (innan við 3 reiti)
            print(mus.nafn + " er nálægt " + rotta1.nafn)
            if mus.afl < rotta1.afl:
                print(rotta1.nafn + " hendir músinni um " + str(rotta1.afl) + " reiti")
                mus.stad -= rotta1.afl  # Viðeigandi rotta slær músina aftur á bak.
            elif mus.afl > rotta1.afl:
                print(mus.nafn + " sigrar " + rotta1.nafn + " því hún er með meira afl")

            else:
                print("Jafntefli á milli " + mus.nafn + " og " + rotta1.nafn)

        elif abs(mus.stad - rotta2.stad) <= 3: # Ef músin er nálægt rotta2 (innan við 3 reiti)
            print(mus.nafn + " er nálægt " + rotta2.nafn)
            if mus.afl < rotta2.afl:
                print(rotta2.nafn + " hendir músinni um " + str(rotta2.afl) + " reiti")
                mus.stad -= rotta2.afl

            elif mus.afl > rotta2.afl:
                print(mus.nafn + " sigrar " + rotta2.nafn + " því hún er með meira afl")

            else:
                print("Jafntefli á milli " + mus.nafn + " og " + rotta2.nafn)
        elif abs(mus.stad - rotta3.stad) <= 3: # Ef músin er nálægt rotta3 (innan við 3 reiti)
            print(mus.nafn + " er nálægt " + rotta3.nafn)
            if mus.afl < rotta3.afl:
                print(rotta3.nafn + " hendir músinni um " + str(rotta3.afl) + " reiti")
                mus.stad -= rotta3.afl

            elif mus.afl > rotta3.afl:
                print(mus.nafn + " sigrar " + rotta3.nafn + " því hún er með meira afl")

            else:
                print("Jafntefli á milli " + mus.nafn + " og " + rotta3.nafn)


    kast = random.randint(1, 6) # Kast einu sinni skilgreint fyrir eftirfarandi if lykkju.
    # Kast er nýtt fyrir hvert nagdýr þó.
    if (nagdyr.teg == "mús"):   # If lykkja fyrir það ef kallað er í mús.
        counter += 1    # Telur hversu oft músin kastar.
        for i in range(kast):   # Hvert skref fyrir sig er athugað og prentað út.
            print("Mús færir sig frá reit", nagdyr.stad, "yfir á reit ", end='')
            mus.stad += 1   # Einu skrefi bætt við, aðein í eina átt fyrir músina.
            print(nagdyr.stad)
            checkIfCombat() # Við hvert skref fyrir sig er svo athugað hvort að rotta sé nálgæt.

            if nagdyr.stad == hamstur.stad: # Nú er athugað hvort að hamstur sé kominn til að henda músinni.
                print("Hamstur kastar mús um", hamstur.afl, "reiti")
                mus.stad += hamstur.afl # Musinni er hent jafn marga reiti og afl hamstursins.
            elif nagdyr.stad == 100:
                break   # Ef músin er kominn á reit 100, klárast leikurinn.

    elif (nagdyr.teg == "rotta"):   # If lykkja fyrir það ef kallað er í rottu.
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



    elif (nagdyr.teg == "hamstur"):   # If lykkja fyrir það ef kallað er í hamstur.
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





# Breytur
kast = 0
fiddy = 0
switchDirection = False
counter = 0
reitir = ''
mus = nagdyr('Mús','mús' , 1 , random.randrange(2,7,2))
rotta1 = nagdyr('Rotta1','rotta' , random.randrange(2,99) , random.randrange(2,7,2))
rotta2 = nagdyr('Rotta2','rotta' , random.randrange(2,99) , random.randrange(2,7,2))
rotta3 = nagdyr('Rotta3','rotta' , random.randrange(2,99) , random.randrange(2,7,2))
hamstur = nagdyr('Hamstur','hamstur' , random.randrange(2,99) , random.randrange(2,7,2))

# Nagdýr kynnt
print(mus.upplysingar())
print(rotta1.upplysingar())
print(rotta2.upplysingar())
print(rotta3.upplysingar())
print(hamstur.upplysingar())


print()
# Hér keyrir leikurinn
while True:
    drawPos()
    action(mus)
    if (mus.stad >= 100): # Ef músin er komin yfir 100 reiti klárast leikurinn.
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
drawPos()
print("Músin kastaði " + str(counter) + " sinnum.")
