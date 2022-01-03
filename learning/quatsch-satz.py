import random

verbs = ['läuft', 'fährt', 'geht', 'tanzt', 'denkt', 'lacht', 'singt', 'schreit', 'ist']
nomen = ['Papa', 'Mama', 'Oma', 'Sid', 'Spenc', 'Tobi', 'Anja']
adverb = ['sehr', '', 'verhältnismäßig', 'kaum', 'viel', 'ziemlich', 'super']
adject = ['schnell', 'flott', 'hübsch', 'gut', 'feucht', 'hüpfend', 'bescheiden', 'langsam', 'lachend', 'pupsend', 'groß']

sentence = ""

for n in range(0, 10):
    sentence += random.choice(nomen) + ' ' + random.choice(verbs) + ' ' + random.choice(adverb) + ' ' + random.choice(adject)  + '.\n'
print(sentence)
