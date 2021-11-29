from ostoskori import Ostoskori
from tuote import Tuote
ostoskori = Ostoskori()
tuote = Tuote("maito", 3)
tuote2 = Tuote("leipä", 5)
ostoskori.lisaa_tuote(tuote)
ostoskori.tyhjenna()
print(ostoskori.ostokset())
print(ostoskori.tavaroita_korissa())