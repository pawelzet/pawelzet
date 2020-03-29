import numpy as np
#wczytuje kolejne rasy
rasy_zwierzat=['papuga', 'ryba', 'nosorozec']
count = ()
while True:
    rasy_zwierzat= input('rasa: ')
    rasy_zwierzat = rasy_zwierzat.lower()
    if not rasy_zwierzat:
        break
 #slownik
imiona=["zyzio","dyzio","nosorozec","nosek"]
zwierzeta_z_rasy = {"papuga":"zyzio", "ryba":"dyzio","nosorozec":"nosek"}#stara wersja
zwiarzeta_z_rasy = {"papuga":["zyzio", "kosmateus"], "ryba":["dyzio", "donald","mariusz","jerzy","gregory"],
                    "nosorozec":["nosek","fif","janusz"],"morswin":["john","jimmy","henry","eustachy"]}#nowa wersja


print(rasy_zwierzat)

#ostatni elemnt z listy
def print_last_in_dict(dictionary):
	for (k, v) in dictionary.items():
		if v:
			print v[-1]

#waga
waga_zwierzecia = {'papuga' : 5, 'ryba' : 100, 'nosorozec' : 200, 'morswin' : 342}

#suma wag
suma = 0
for key in zwierzeta_z_rasy:
    suma += waga_zwierzecia[key]


# czesc druga
# zadanie zje_mnie
zje_mnie = {'swierszcz' : ['mysz'],
	'mysz' : ['kot', 'waz'],
	'kot' : ['waz'],
	'waz' : ['kot', 'orzel'],
	'orzel' : ['morswin'],
	'morswin' : [],
	}
print(zje_mnie)

def znajdz_lancuch_pokarmowy_a(animal, chain):
	print ("searching "),  animal
	for k in zje_mnie:
		if k == animal:
			chain.append(k)
			list_of_predators = zje_mnie[k]
			predator = None
			# nieznaloziony to find, if byl find to search...
			for next_predator in list_of_predators:
				if next_predator not in chain:
		           #jak znazlem
					predator = next_predator
					break


def znajdz_lancuch_pokarmowy(animal):
	chain = []
	znajdz_lancuch_pokarmowy_a(animal, chain)
	return chain

def print_chain(animal_chain):
	print ("<-").join(animal_chain)

chain = znajdz_lancuch_pokarmowy('swierszcz')
print_chain(chain)

przykladowe_zwierzeta = {
	'swierszcz' : ['swierszcz_janek', 'swierszcz_bolek'],
	'mysz' : ['mysz_janek', 'mysz_bolek'],
	'kot' : ['kot_janek', 'kot_bolek'],
	'waz' : ['waz_janek', 'waz_bolek'],
	'orzel' : [],
#	'orzel' : ['orzel_janek', 'orzel_bolek'], # w bazie zabraklo orlow
	'morswin' : ['morswin_janek', 'morswin_bolek']
}



