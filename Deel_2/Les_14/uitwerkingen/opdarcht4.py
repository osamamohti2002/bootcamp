woordenlijst = []

for i in range(5):
  woord = input(f'voer woord {i+1} in')
  woordenlijst.append(woord)


print(f'de ingevoerd woorden zijn:{woordenlijst}')

for woord in woordenlijst:
    print(woord)