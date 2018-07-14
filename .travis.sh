#!/usr/bin/env bash

# Copied from the IRkernel repo
# https://github.com/IRkernel/IRkernel/blob/master/.travis.sh

create_conda_environment() (
    set -ex

    # http://conda.pydata.org/docs/travis.html
    wget "https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh" -O miniconda.sh
    bash miniconda.sh -b -p "$HOME/miniconda"
    rm miniconda.sh # needed to prevent a error in the R CMD check part

    hash -r
    conda config --set always_yes yes --set changeps1 no
    conda update -q conda
    # Useful for debugging any issues with conda
    conda info -a
    conda create -q -n test-environment python=3.6 pip jupyter pytest

    ls ~/miniconda/bin
)
