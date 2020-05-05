#!/usr/local/bin/zsh

for f in *.ipynb;
    jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace $f
