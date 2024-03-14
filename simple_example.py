from get_similarity import get_simil, sim_by_file
import warnings
import json

warnings.filterwarnings('ignore')

print("-"*20)
print("Avec deux strings")
print("-"*20)

s1 = "Je mange le Lapin"
s2 = "Ie mange le lapin vert"

res = get_simil([s1, s2])
print(json.dumps(res, indent =2))

#On peut aussi comparer une chaîne à plusieurs chaînes, la première sert alors de "référence"
print("-"*20)
print("Trois chaînes, la première est comparée aux deux autres")
print("-"*20)

s1 = "Je mange le Lapin"
s2 = "Ie mange le lapin vert"
s3 = "Il mange les lapin vert"

res = get_simil([s1, s2, s3])
print(json.dumps(res, indent =2))

#On peut aussi "nommer" les fichiers hypothèses (la première est la référence)
print("avec des 'noms' pour les fichiers")
res = get_simil([s1, s2, s3], ["Nom 1", "Nom 2"])
print(json.dumps(res, indent =2))

print("-"*20)
print("Avec des chemins de fichiers et une partie des métriques")
print("-"*20)

path_ref = "dummy_data/reference/20111110_www.express.gr_6731493104b964ea9ee16b34b11871b08ddca1452726df3e47a44c93"
path_hyp1 = "dummy_data/cleaned/TRAF/20111110_www.express.gr_6731493104b964ea9ee16b34b11871b08ddca1452726df3e47a44c93"
path_hyp2 = "dummy_data/cleaned/BP3/20111110_www.express.gr_6731493104b964ea9ee16b34b11871b08ddca1452726df3e47a44c93"

#le paramètre all_metrics peut être à False pour limiter le nombre de mesures calculées

res = sim_by_file([path_ref, path_hyp1, path_hyp2], all_metrics=False)

print(json.dumps(res, indent =2))


