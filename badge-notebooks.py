import glob
import json
import sys
import os

remove = False
if len(sys.argv) == 2:
    if sys.argv[1] == 'remove':
        remove = True

fnames = glob.glob('*.ipynb')

for fname in fnames:
    dirname = os.path.basename(os.path.dirname(os.path.abspath(fname)))

    with open(fname, "rt", encoding="utf-8") as inf:
        d = json.load(inf)

    s = fr'<a href="https://colab.research.google.com/github/lukeolson/imperial-multigrid/blob/master/{dirname}/{fname}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'
    #s = fr'[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lukeolson/imperial-multigrid/blob/master/{dirname}/{fname})'
    newcell = {}
    newcell['cell_type'] = "markdown"
    newcell['metadata'] = {"colab_type": "text",
                           "id": "colab-badge"}
    newcell['source'] = [s]

    topcell = d['cells'][0]
    doit = False
    if 'id' in topcell['metadata'].keys():
        if topcell['metadata']['id'] != 'colab-badge':
            doit = True
        else:
            print(f'{fname}: already badged')
            if remove:
                d['cells'].pop(0)
    else:
        doit = True

    if doit:
        d['cells'].insert(0, newcell)

    with open(fname, "wt") as outf:
        json.dump(d, outf, indent=1, sort_keys=True)
        outf.write("\n")
