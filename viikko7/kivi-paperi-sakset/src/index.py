from kaynnista import kaynnista
def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        if vastaus.endswith("a"):
            vastaus = "kaksinpeli"
        elif vastaus.endswith("b"):
            vastaus = "yksinpeli"
        elif vastaus.endswith("c"):
            vastaus = "haastava_yksinpeli"
        else:
            break
        kaynnista(vastaus)


if __name__ == "__main__":
    main()
