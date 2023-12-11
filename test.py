from get_similarity import process_data

path_hyp = "dummy_data/cleaned/"
path_ref = "dummy_data/reference/"
res = process_data(path_hyp, path_ref)


import json
print(json.dumps(res, indent =2))
