import sys
import glob
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def open_file(path):
  with open(path, encoding="utf-8") as f:
    content = f.read()
  return content

def get_simil(corpus, names = []):
  if len(names)<len(corpus)-1:
    names = [x for x in range(len(corpus)-1)]
  vectorizer = CountVectorizer(analyzer ="word", ngram_range=(1,2))
  X = vectorizer.fit_transform(corpus)
  array = X.toarray()
  simil = cosine_similarity(array)[0][1:]
  dic = {"cosine": {names[i]:simil[i] for i in range(len(names))}}
  return dic 
  #output 1: simil, output 2: similar syst.(closer together than to the ref)
path_hyp = sys.argv[1]
path_ref = sys.argv[2]

all_hyp = glob.glob(f"{path_hyp}/*/*")
all_ref = glob.glob(f"{path_ref}/*")

data = {re.split("/", path)[-1]:{"ref": path, "hyp":[]} for path in all_ref}
for path in all_hyp:
  filename = re.split("/", path)[-1]
  data[filename]["hyp"].append(path)


results = {}
for filename, dic in data.items():

  hyp_path = sorted([path for path in dic["hyp"]])
  hyp_names = [re.split("/", path)[-2] for path in hyp_path]
  corpus = [open_file(dic["ref"])]
  corpus += [open_file(path) for path in hyp_path]
  dic_simil = get_simil(corpus, names=hyp_names)
  for metric, d in dic_simil.items():
    results.setdefault(metric, {})
    for name, res in d.items():
      results[metric].setdefault(name, [])
      results[metric][name].append(res)


import statistics as st

dic_agreg = {}
for metric, dic_syst in results.items():
  dic_agreg.setdefault(metric, {"mean":[]})
  for syst, l_res in dic_syst.items():
    dic_agreg[metric]["mean"].append([st.mean(l_res), syst])
  print(metric)
  print(sorted(dic_agreg[metric]["mean"], reverse=True))

