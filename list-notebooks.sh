#!/usr/local/bin/zsh

for f in lecture-1-mg-basics/*.ipynb;
    echo '- ['$f:t']''( https://colab.research.google.com/github/lukeolson/imperial-multigrid/blob/master/'$f')'
