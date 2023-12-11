example : try test.py

from get_similarity import process_data

path_hyp = "dummy_data/cleaned/"# your path to the reference data
path_ref = "dummy_data/reference/"#your path to the hypothesis (one directory for each different hypothesis)
# NB: the filenames must be the same

res = process_data(path_hyp, path_ref)


Expected directory structure (NB: the reference data has to be called reference, the hypothesis directory can have any name):


dummy_data/
├── cleaned
│   ├── BP3
│   │   ├── 20111101_www.express.gr_6648058818bdb924afb68d540f362451eec0e42a8d47455b17b6ca3e
│   │   ├── 20111103_www.express.gr_00432316609d53b9b165a50c0f43ba303c9d4babab967870dac4c878
│   │   ├── 20111103_www.express.gr_b790b5da5f6a30c85f59855f847023204bb8b8f289a2c430be3f8e10
│   │   ├── 20111103_www.express.gr_c61012b55d72b56911132fdce606fca3b88af9af03cbfd839df60fcf
│   │   ├── 20111104_www.express.gr_374193c3be99145c215b4474444c811d3f83b20ab84040d701ee7a21
│   │   ├── .... 
│   ├── READABILITY
│   │   ├── 20111101_www.express.gr_6648058818bdb924afb68d540f362451eec0e42a8d47455b17b6ca3e
│   │   ├── 20111103_www.express.gr_00432316609d53b9b165a50c0f43ba303c9d4babab967870dac4c878
│   │   ├── 20111103_www.express.gr_b790b5da5f6a30c85f59855f847023204bb8b8f289a2c430be3f8e10
│   │   ├── 20111103_www.express.gr_c61012b55d72b56911132fdce606fca3b88af9af03cbfd839df60fcf
│   │   ├── 20111104_www.express.gr_374193c3be99145c215b4474444c811d3f83b20ab84040d701ee7a21
│   │   ├── .... 
│   └── TRAF
│       ├── 20111101_www.express.gr_6648058818bdb924afb68d540f362451eec0e42a8d47455b17b6ca3e
│       ├── 20111103_www.express.gr_00432316609d53b9b165a50c0f43ba303c9d4babab967870dac4c878
│       ├── 20111103_www.express.gr_b790b5da5f6a30c85f59855f847023204bb8b8f289a2c430be3f8e10
│       ├── 20111103_www.express.gr_c61012b55d72b56911132fdce606fca3b88af9af03cbfd839df60fcf
│       ├── 20111104_www.express.gr_374193c3be99145c215b4474444c811d3f83b20ab84040d701ee7a21
│   │   ├── .... 
└── reference
    ├── 20111101_www.express.gr_6648058818bdb924afb68d540f362451eec0e42a8d47455b17b6ca3e
    ├── 20111103_www.express.gr_00432316609d53b9b165a50c0f43ba303c9d4babab967870dac4c878
    ├── 20111103_www.express.gr_b790b5da5f6a30c85f59855f847023204bb8b8f289a2c430be3f8e10
    ├── 20111103_www.express.gr_c61012b55d72b56911132fdce606fca3b88af9af03cbfd839df60fcf
    ├── 20111104_www.express.gr_374193c3be99145c215b4474444c811d3f83b20ab84040d701ee7a21
    ├── ....
