# R in Jupyter with Binder

An example of how to use R in Jupyter notebooks and then make a Binder environment to run them interactively on the web.
This repo was inspired from [a Tweet](https://twitter.com/Alex_Danvers/status/1016395766250627072) in a discussion about [Episode 7 of The Bayes Factor podcast](https://sites.tufts.edu/hilab/podcast/liz-page-gould-and-alex-danvers/).

> Disclaimer: I am a Python programmer, and I don't use R. This is just what I know from being able to read code and understanding how Jupyter works.

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Build Status](https://travis-ci.com/matthewfeickert/R-in-Jupyter-with-Binder.svg?branch=master)](https://travis-ci.com/matthewfeickert/R-in-Jupyter-with-Binder)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/matthewfeickert/R-in-Jupyter-with-Binder/master)

## Check it out first

Before learning how to setup R in Jupyter, first go check out how cool it is in Binder! Just click the "launch Binder" badge above.

## Table of contents

- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Using papermill with Jupyter](#using-papermill-with-jupyter)
- [Setting up a minimal Binderfile](#setting-up-a-minimal-binderfile)
- [Further Reading](#further-reading)

## Requirements

Before you can begin you need to make sure that you have the following in your working environment
- [Jupyter](http://jupyter.org/)
- A modern version of [R](https://www.r-project.org/)

## Setup and Installation

### Install Jupyter

- Install Jupyter

### Install R

- Install R

### Install the R kernel for Jupyter (IRkernel)

- Install the [R kernel for Jupyter](https://github.com/IRkernel/IRkernel) ([IRkernel](https://irkernel.github.io/))

## Using papermill with Jupyter

- [papermill](https://github.com/nteract/papermill)
- Install [R bindings for Papermill](https://github.com/nteract/papermillr)

## Setting up a minimal Binderfile

- [Binder](https://mybinder.org/)
- [Specifying an R environment with a runtime.txt file](https://mybinder.readthedocs.io/en/latest/sample_repos.html#specifying-an-r-environment-with-a-runtime-txt-file)
   - Example Jupyter+R environment on Binder: [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/binder-examples/r/master?filepath=index.ipynb)

## Further Reading and Resources

- [Jupyter And R Markdown: Notebooks With R](https://www.datacamp.com/community/blog/jupyter-notebook-r), by [Karlijn Willems](https://github.com/Kacawi)
- [Rocker](https://www.rocker-project.org/)'s [R configurations for Docker repo](https://github.com/rocker-org/rocker)
- [rOpenSci](https://ropensci.org/)
