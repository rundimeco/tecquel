from get_similarity import process_by_source
import glob
import sys

if len(sys.argv)==2:
  path_sources = sys.argv[1]
else:
  path_sources = "dummy_data_by_source/"

process_by_source(path_sources)
