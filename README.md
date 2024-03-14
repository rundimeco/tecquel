## Simple example : simple_example.py

usage :

from get_similarity import get_simil, sim_by_file

s1 = "Je mange le Lapin"
s2 = "Ie mange le lapin vert"

res = get_simil([s1, s2])

On peut aussi comparer s1 à plsuieurs chaînes :

res = get_simil([s1, s2, s3, s4])

On peut travailler avec des chemins de fichiers :

res = sim_by_file([path_ref, path_hyp])

comparer le fichier dont le chemin est path_ref au fichier dont le chemin est path_hyp

## Example with a more complex directory structure (useful for web scraping an dOCR when one compares multiple systems)

example : try test.py

from get_similarity import process_data

path_hyp = "dummy_data/reference/"# your path to the reference data
path_ref = "dummy_data/cleaned/"#your path to the hypothesis (one directory for each different hypothesis)


NB: the filenames must be the same in teh "reference dir" and all the hypothesis dirs

res = process_data(path_hyp, path_ref)

Here: explain vocabulary

Expected directory structures

Option 1 : Directory structure Driven by tools
all files of a given tool are in the same directory

 Give a directory with the reference data and another directory with all the hypothesis in their own directory. Each filename in the reference data and in the reference corpus must have the name.

USAGE (see test.py):
from get_similarity import process_data

path_hyp = "dummy_data/cleaned/"
path_ref = "dummy_data/reference/"

print(f"Processing {path_ref} as reference path")
print(f"Processing {path_hyp} as hypothesis path")
res = process_data(path_hyp, path_ref)

Each filename of each hypothesis with be matched with the corresponding reference file

See "dummy_data" as an example of teh structure

dummy_data/ contains two subdirectories (reference and cleaned)
- reference contains the reference files
- cleaned contains different hypothesis obtained with different tools (BP3, GOO ...)

dummy_data/
├── cleaned
│   ├── BP3
│   ├── GOO
│   ├── HTML2TEXT
│   ├── INSCRIPTIS
│   ├── JT
│   ├── NEWSPAPER
│   ├── READABILITY
│   └── TRAF
└── reference



Option 2 : Directory structure Driven by source (or books)
The files are first sorted by source and then by tool.
Then there is a directory with the reference (REF) and all the hypothesis (HYP) 

You can find an example in the dummy_data_by_source directory:


dummy_data_by_source/
└── goodcontents.net
    ├── HYP
    │   └── NEWSPAPER
    │       └── TXT
    │           └── 20111121_goodcontents.net_6e8a193b0d5e43883d5bcacdf...
    └── REF
        └── TXT
            └── 20111121_goodcontents.net_6e8a193b0d5e43883d5bcacdf...
