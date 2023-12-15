import glob
import json
import sys
import re

path_in=""
if len(sys.argv)==2:
  path_in = sys.argv[1]
elif path_in=="":
  print("specify the path_in\n exiting....")
  exit()
path_json = glob.glob(f"{path_in}*")

out = {}
for path in path_json:
  out.setdefault(path, {})
  with open(path) as f:
    dic = json.load(f)
  for metric, l_res in dic.items():
    for val, config in l_res:
      modele = re.split("modele==", config)[1]
      out[path].setdefault(modele, {})
      out[path][modele][metric] = round(val, 4)

print(json.dumps(out))
l_path = sorted(out.keys())

print("\t".join(["path", "modele"]+sorted(out[path][modele].keys())))
for path in l_path:
  line = [path]
  for modele in sorted(out[path].keys()):
    line.append(modele)
    for name in sorted(out[path][modele].keys()):
      line.append(str(out[path][modele][name]))
  print("\t".join(line))
