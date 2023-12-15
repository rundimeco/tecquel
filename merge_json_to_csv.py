import glob
import json
import sys
import re

def merge_json(path_json, path_out = "resullts_files_merged"):
  if len(path_json)==0:
      print("This function needs a list of path")
      print("The list is empty\n exiting ....")
      exit()
  out = {}
  for path in path_json:
    out.setdefault(path, {})
    with open(path) as f:
      dic = json.load(f)
    for metric, l_res in dic.items():
      for val, modele in l_res:
        out[path].setdefault(modele, {})
        out[path][modele][metric] = round(val, 4)
  with open(f"{path_out}.json", "w") as w:
      w.write(json.dumps(out, indent =2))
  print(f"Output JSON: {path_out}.json")

  l_path = sorted(out.keys())
  out_tsv = ["\t".join(["path", "modele"]+sorted(out[path][modele].keys()))]
  for path in l_path:
    line = [path]
    for modele in sorted(out[path].keys()):
      line.append(modele)
      for name in sorted(out[path][modele].keys()):
        line.append(str(out[path][modele][name]))
    out_tsv.append("\t".join(line))
  with open(f"{path_out}.tsv", "w") as w:
      w.write("\n".join(out_tsv))
  print(f"Output tsv: {path_out}.tsv")


if __name__=="__main__":
  print("test merge with dummy_data")
  liste = glob.glob("RESULTS/dummy*")
  merge_json(liste, path_out = "all_results_dummy_data")
