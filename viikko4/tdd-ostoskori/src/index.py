from ostoskori import Ostoskori
from tuote import Tuote
ostoskori = Ostoskori()
tuote = Tuote("maito", 3)
tuote2 = Tuote("leipä", 5)
ostoskori.lisaa_tuote(tuote)
ostoskori.lisaa_tuote(tuote2)
print(ostoskori.ostokset())
print(len(ostoskori.ostokset()))