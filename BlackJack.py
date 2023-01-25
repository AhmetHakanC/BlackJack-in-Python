import random

kart_degerleri = {"Sinek 2": 2, "Sinek 3": 3, "Sinek 4": 4, "Sinek 5": 5, "Sinek 6": 6, "Sinek 7": 7, "Sinek 8": 8,
                  "Sinek 9": 9, "Sinek 10": 10, "Sinek Joker": 10, "Sinek Kız": 10, "Sinek Kral": 10,
                  "Sinek As": 1,
                  "Maça 2": 2, "Maça 3": 3, "Maça 4": 4, "Maça 5": 5, "Maça 6": 6, "Maça 7": 7, "Maça 8": 8,
                  "Maça 9": 9, "Maça 10": 10, "Maça Joker": 10, "Maça Kız": 10, "Maça Kral": 10, "Maça As": 1,
                  "Karo 2": 2, "Karo 3": 3, "Karo 4": 4, "Karo 5": 5, "Karo 6": 6, "Karo 7": 7, "Karo 8": 8,
                  "Karo 9": 9, "Karo 10": 10, "Karo Joker": 10, "Karo Kız": 10, "Karo Kral": 10, "Karo As": 1,
                  "Kupa 2": 2, "Kupa 3": 3, "Kupa 4": 4, "Kupa 5": 5, "Kupa 6": 6, "Kupa 7": 7, "Kupa 8": 8,
                  "Kupa 9": 9, "Kupa 10": 10, "Kupa Joker": 10, "Kupa Kız": 10, "Kupa Kral": 10, "Kupa As": 1}


def create_deck():
    simgeler = ["Sinek", "Maça", "Karo", "Kupa"]
    sayilar = ["As", "Joker", "Kız", "Kral", 2, 3, 4, 5, 6, 7, 8, 9, 10]
    kagitlar = []

    for i in range(3):
        for simge in simgeler:
            for sayi in sayilar:
                kagitlar.append(simge + " " + str(sayi))
    random.shuffle(kagitlar)

    return kagitlar


def deal_cards(deck):
    player_cards = []
    dealer_cards = []

    for i in range(2):
        player_cards.append(deck.pop())
        dealer_cards.append(deck.pop())

    return player_cards, dealer_cards


def hand_value(cards):
    value = ace = 0

    if type(cards) == list:
        for card in cards:
            value += kart_degerleri[card]
            if kart_degerleri[card] == 1:
                ace += 1

        if value - 1 < 11 and ace >= 1:
            value += 10

        return value
    else:
        return kart_degerleri[cards]


def ekran(cards):
    value = hand_value(cards)

    for card in cards:
        print(card, end=" | ")
    print("--> Toplam: " + str(value))


# Made By: @AhmetHakanC on GitHub
def game():
    oyuncu_skor = 0
    banka_skor = 0

    print("Welcome to Hakan's BlackJack!")
    print("İsminizi giriniz: ")
    name = input()
    if name == "":
        name = "Player"

    print("Merhaba " + name + "!")

    # Bakiye alınıyor
    while True:
        print("Bakiyenizi giriniz: ")
        bakiye = input()
        try:
            bakiye = int(bakiye)
        except ValueError:
            print("Lütfen bir sayı giriniz!")
            continue
        else:
            print("Bakiyeniz: " + str(bakiye))
            break

    print("Oyun başlıyor...")

    # Oyun başlıyor
    while True:
        bj = False
        # Bahis alınıyor
        while True:
            print("Bahis miktarınızı giriniz: ")
            bahis = input()
            try:
                bahis = int(bahis)
            except ValueError:
                print("Lütfen bir sayı giriniz!")
                continue
            else:
                if bahis > bakiye:
                    print("Bakiyeniz yetersiz!")
                    continue
                else:
                    print("Bahis miktarınız: " + str(bahis))
                    break

        deck = create_deck()

        print("Kartlar dağıtılıyor...")
        player_cards, dealer_cards = deal_cards(deck)

        if hand_value(player_cards) == 21:
            bj = True
            bahis = bahis * 1.5

        print("Kasa'nın kartları: ")
        print(dealer_cards[0], " | ", "Kapalı")

        print()

        print("Kartlarınız: ")
        ekran(player_cards)

        choice = ""
        while True:
            if not bj:
                if hand_value(player_cards) == 11 and len(player_cards) == 2:
                    print("Bahsi 2'ye katlamak ister misiniz? (E/H)")
                    choice = input()
                    choice = choice.upper()
                    if choice == "E":
                        bahis *= 2
                    else:
                        continue
                if choice == "E":
                    choice = "H"
                else:
                    print("Hit mi Stay mi? (H/S)")
                    choice = input()
                    choice = choice.upper()
            if choice == "H":
                player_cards.append(deck.pop())
                ekran(player_cards)
                if hand_value(player_cards) > 21:
                    print("Bust!")
                    bakiye -= bahis
                    break
                elif hand_value(player_cards) == 21:
                    print("BlackJack!")
                    bj = True
                    choice = "S"
            elif choice == "S":
                ekran(dealer_cards)
                while hand_value(dealer_cards) < 17:
                    dealer_cards.append(deck.pop())
                    ekran(dealer_cards)
                if hand_value(dealer_cards) > 21:
                    print("Kasa Bust!")
                    bakiye += bahis
                    oyuncu_skor += 1
                    break
                elif hand_value(dealer_cards) > hand_value(player_cards):
                    print("Kasa kazandı")
                    bakiye -= bahis
                    banka_skor += 1
                    break
                elif hand_value(dealer_cards) < hand_value(player_cards):
                    print("Kazandınız!")
                    bakiye += bahis
                    oyuncu_skor += 1
                    break
                else:
                    print("Berabere!")
                    break
            else:
                print("Hatalı giriş!")
                continue

        print("Bakiyeniz: " + str(bakiye))
        if bakiye == 0:
            print("Bakiyeniz bitti!")
            break
        else:
            print("Tekrar oynamak ister misiniz? (E/H)")
            choice = input()
            choice = choice.upper()
            if choice == "E":
                continue
            elif choice == "H":
                break
            else:
                print("Hatalı giriş!")
                continue

    print("\n")
    print("Oynanan oyun sayısı: " + str(oyuncu_skor + banka_skor))
    print("Oyuncu skoru: " + str(oyuncu_skor))
    print("Banka skoru: " + str(banka_skor))
    print(name, "oyuncusunun kazanma ihtimali: " + str(oyuncu_skor / (oyuncu_skor + banka_skor) * 100) + "%")



game()

