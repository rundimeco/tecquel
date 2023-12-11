from get_similarity import process_data

path_hyp = "dummy_data/cleaned/"
path_ref = "dummy_data/reference/"

print(f"Processing {path_ref} as reference path")
print(f"Processing {path_hyp} as hypothesis path")
res = process_data(path_hyp, path_ref)

#chaque livre HYP REF

import json
print(json.dumps(res, indent =2))
