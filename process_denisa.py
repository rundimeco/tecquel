from merge_json_to_csv import merge_json
import glob

liste_path = glob.glob("RESULTS/data*")
merge_json(liste_path)
