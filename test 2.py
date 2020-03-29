# czesc druga
# zadanie zje_mnie
zje_mnie = {'swierszcz' : ['mysz'],
	'mysz' : ['kot', 'waz'],
	'kot' : ['waz'],
	'waz' : ['kot', 'orzel'],
	'orzel' : ['morswin'],
	'morswin' : [], # morswin krol wszystkich zwierzat
	}
print(zje_mnie)

def znajdz_lancuch_pokarmowy_rec(animal, chain):
	print ("searching "),  animal
	for k in zje_mnie:
		if k == animal:
			chain.append(k)
			list_of_predators = zje_mnie[k]
			predator = None
			# nieznaloziony find, if byl to search...
			for next_predator in list_of_predators:
				if next_predator not in chain:
		           #jak znazlem
					predator = next_predator
					break
			#
			znajdz_lancuch_pokarmowy_rec(predator, chain)

def znajdz_lancuch_pokarmowy(animal):
	chain = []
	znajdz_lancuch_pokarmowy_rec(animal, chain)
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
