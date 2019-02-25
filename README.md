# R in Jupyter with Binder

An example of how to use R in Jupyter notebooks and then make a Binder environment to run them interactively on the web.
This repo was inspired from [a Tweet](https://twitter.com/Alex_Danvers/status/1016395766250627072) in a discussion about [Episode 7 of The Bayes Factor podcast](https://sites.tufts.edu/hilab/podcast/liz-page-gould-and-alex-danvers/).

> Disclaimer: I am a physicist and primarily a Python and C++ programmer and I don't use/know R. This repo is just what I know from being able to read code and understanding how Jupyter works.

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![DOI](https://zenodo.org/badge/140347900.svg)](https://zenodo.org/badge/latestdoi/140347900)
[![Build Status](https://travis-ci.com/matthewfeickert/R-in-Jupyter-with-Binder.svg?branch=master)](https://travis-ci.com/matthewfeickert/R-in-Jupyter-with-Binder)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/matthewfeickert/R-in-Jupyter-with-Binder/master?filepath=R-in-Jupyter-Example.ipynb)

## Check it out first

Before learning how to setup R in Jupyter, first go check out how cool it is in Binder! Just click the "launch Binder" badge above.

## Table of contents

- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Enable package dependency management with packrat](#enable-package-dependency-management-with-packrat)
- [Using papermill with Jupyter](#using-papermill-with-jupyter)
- [Testing Jupyter notebooks with pytest](#testing-jupyter-notebooks-with-pytest)
- [Automating testing alongside development with CI](#automating-testing-alongside-development-with-ci)
- [Setting up a Binder environment](#setting-up-a-binder-environment)
- [Preservation and DOI with Zenodo](#preservation-and-doi-with-zenodo)
- [R Markdown in Jupyter with jupytext](#r-markdown-in-jupyter-with-jupytext)
- [Further Reading and Resources](#further-reading-and-resources)
- [Acknowledgements](#acknowledgements)

## Requirements

Before you can begin you need to make sure that you have the following in your working environment
- [Jupyter](http://jupyter.org/)
- A modern version of [R](https://www.r-project.org/)

## Setup and Installation

- [Install Jupyter](http://jupyter.org/install)
   - If you aren't familiar with Python and `pip` then just follow the instructions for installing with Anaconda
- [Install R](https://cran.r-project.org/doc/manuals/r-release/R-admin.html)
- Install the [R kernel for Jupyter](https://github.com/IRkernel/IRkernel) ([IRkernel](https://irkernel.github.io/))

## Enable package dependency management with [packrat](https://github.com/rstudio/packrat)

The first step in any project should be making sure that the library dependencies are specified and reproducible. This can be done in R with the [packrat](https://rstudio.github.io/packrat/) library.

First install packrat

```shell
R -e 'install.packages("packrat")'
```

Then from your project directory initialize Packrat for your project

```shell
R -e 'packrat::init()'
```

which will determine the R libraries used in your project and then build the list of dependencies for you. This effectively creates an isolated computing environment (known as "virtual environments" it other programming languages).

Running `packrat::init()` results in the directory `packrat` being created with the files `init.R`, `packrat.lock` and `packrat.opts` inside of it. It will additionally also create or edit a project `.Rprofile` and edit any existing `.gitignore` file. The following files should be kept under version control for your project to be reproducible anywhere:

- `.Rprofile`
- `packrat/init.R`
- `packrat/packrat.lock`
- `packrat/packrat.opts`

As you work on your project and use more libraries you can [update your dependencies managed by `packrat`](https://rstudio.github.io/packrat/walkthrough.html) with (inside the R environment)

```r
packrat::snapshot()
```

which updates `packrat/packrat.lock` and `packrat/packrat.opts`. You can also check if you have introduces new dependencies with

```r
packrat::status()
```

If you remove libraries from use that were managed by `packrat` you can check this with

```r
packrat::status()
```

and then remove them from `packrat` with

```r
packrat::clean()
```

to ensure the minimal environment necessary for reproducibility is kept. Checking the status should now show

```r
packrat::status()
#> Up to date.
```

If you have a `packrat.lock` file that you want to create an environment from that doesn't already exist you can build the environment by running (from the command line)

```shell
R -e 'packrat::restore()'
```

This is one way in which you could setup the same `packrat` environment on a different machine from the Git repository.

## Using [papermill](https://github.com/nteract/papermill) with Jupyter

> Papermill is a tool for parameterizing, executing, and analyzing Jupyter Notebooks.

This means that you can use [papermill](https://github.com/nteract/papermill) to _externally_ run, manipulate, and test Jupyter notebooks. This allows you to use Jupyter notebooks as components of an automated data analysis pipeline or for procedurally testing variations.

- To use with Jupyter notebooks running in the IRkernel [install the R bindings for papermill (`papermillR`)](https://github.com/nteract/papermillr)

A toy example of how to use papermill is demonstrated in the [example Jupyter notebook](https://github.com/matthewfeickert/R-in-Jupyter-with-Binder/blob/master/R-in-Jupyter-Example.ipynb).

## Testing Jupyter notebooks with [pytest](https://docs.pytest.org/en/latest/)

To provide testing for Jupyter notebooks we can use [pytest](https://docs.pytest.org/en/latest/) in combination with papermill.

- [Install pytest](https://docs.pytest.org/en/latest/getting-started.html)
   - If you installed Jupyter with Conda then you can also [install pytest with Conda](https://anaconda.org/anaconda/pytest)

Once you have installed pytest and done some [minimal reading of the docs](https://docs.pytest.org/en/latest/getting-started.html#create-your-first-test) then create a `tests` directory and write your test files in Python inside of it.

An example of some very simple tests using papermill is provided in [`tests/test_notebooks.py`](https://github.com/matthewfeickert/R-in-Jupyter-with-Binder/blob/master/tests/test_notebooks.py). Once you read though and understand what the testing file is doing execute the tests with `pytest` in the top level directory of the repo by running

```shell
pytest
```

To see the output that the individual testing functions would normally [print to `stdout`](https://docs.pytest.org/en/latest/capture.html) run with the `-s` flag

```shell
pytest -s
```

### Why write tests?

There are numerous reasons to test your code, but as a scientist an obvious one is ensured reproducibility of experimental results. If your analysis code has unit tests and the analysis itself exists in an automatically testable pipeline then you and your colleagues should have more confidence in your analysis. Additionally, your analysis becomes (by necessity) a well documented and transparent process.

Want to learn more? Check out the [Test and Code podcast](http://testandcode.com/) hosted by [Brian Okken](https://github.com/okken).

### Why test with pytest?

pytest is the most comprehensive and scalable testing framework that I know of. I am biased, but I continue to be impressed with how nimble, powerful, and easy it is to work with. It makes me want to write tests. For the purposes of this demo repository it is also important as it allows for writing tests that use papermill (papermill's `execute_notebook` is only accessible through the [Python API](http://papermill.readthedocs.io/en/latest/usage.html#execute-via-the-python-api)).

There are testing frameworks in R, most notably [testthat](https://github.com/r-lib/testthat), which I assume are good. So I would encourage you to explore those as well.

## Automating testing alongside development with CI

Assuming that you're using Git to develop your analysis code then you can have a continuous integration service (such as [Travis CI](https://travis-ci.org/) or [CircleCI](https://circleci.com/)) automatically test your code in a fresh environment every time you push to GitHub. Testing with CI is a great way to know that your analysis code is working exactly as expected in a reproducible environment from installation all the way through execution as you develop, revise, and improve it. To see the output of the build/install and testing of this repo in Travis click on the build status badge at the top of the `README` (also here: [![Build Status](https://travis-ci.com/matthewfeickert/R-in-Jupyter-with-Binder.svg?branch=master)](https://travis-ci.com/matthewfeickert/R-in-Jupyter-with-Binder)).

To start off with I would recommend using Travis CI (it is the easiest to get up and running).

- [Getting started with Travis CI](https://docs.travis-ci.com/user/getting-started/)
- Example [`.travis.yml`](https://github.com/matthewfeickert/R-in-Jupyter-with-Binder/blob/master/.travis.yml) in this repo
- [Travis CI docs on writing YAML CI files for R](https://docs.travis-ci.com/user/languages/r/)

### Access restrictions and hosting

There may be instances where you want to have your Git repository be private until work is complete or other information is made publicly available, and you still want to be able to use CI services.

Travis CI (currently) only works with GitHub and is [free only for public repositories](https://travis-ci.com/plans). CircleCI works with any Git web hosting service (i.e., GitHub, GitLab, Bitbucket) and allows for free use with public and private repositories [up to a monthly use time budget](https://circleci.com/pricing/).
Additionally, GitLab offers [their own CI service](https://docs.gitlab.com/ee/ci/README.html) that is integrated into the GitLab platform. If your organization self-hosts an instance of GitLab (GitLab is [open core](https://about.gitlab.com/pricing/)) then you can use those CI tools with your private GitLab hosted repositories. If your organization has access to the enterprise version of GitLab then you can even run [GitLab CI on GitHub hosted repositories](https://docs.gitlab.com/ee/ci/ci_cd_for_external_repos/github_integration.html).

## Setting up a [Binder](https://mybinder.org/) environment

[Binder](https://mybinder.org/) turns your GitHub repository into a fully interactive computational environment (as you hopefully have already seen from the demo notebook). It then allows people to run any code that exists in the repository from their web browser without having to install any code and is a great tool for collaboration and sharing results.

The Binder team has done amazing work to make "Binderizing" a GitHub repository as simple as possible. In the case of getting an R computing environment many times all that you need (in addition to a `DESCRIPTION` file and maybe an `install.R`) is a `runtime.txt` file that dictates which daily snapshot of [MRAN](https://mran.microsoft.com/documents/rro/reproducibility) to use. See the [`binder`](https://github.com/matthewfeickert/R-in-Jupyter-with-Binder/tree/master/binder) directory for an example of what is needed to get this repository to run in Binder.

- [Specifying an R environment with a runtime.txt file](https://mybinder.readthedocs.io/en/latest/sample_repos.html#specifying-an-r-environment-with-a-runtime-txt-file)
   - Example Jupyter+R environment on Binder: [![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/r/master?filepath=index.ipynb)
- [Binder FAQs](https://mybinder.readthedocs.io/en/latest/faq.html)

You'll note that the "launch Binder" badge at the top of the `README` automatically launches into the `R-in-Jupyter-Example.ipynb` notebook. This was configured to do so, but the default Binder behavior is to launch the Jupyter server and then show the directory structure of the repository.

To see that behavior launch Binder from here: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/matthewfeickert/R-in-Jupyter-with-Binder/master)

Once the server loads click on any file to open it in an editor or as a Jupyter notebook.

## Preservation and DOI with [Zenodo](https://zenodo.org/)

To further make your analysis code more robust you can preserve it and make it [citable by getting a DOI](https://guides.github.com/activities/citable-code/) for the project repository with [Zenodo](https://zenodo.org/). Activating version tracking on your GitHub repository with Zenodo will allow it to automatically freeze a version of the repository with each new version tag and then archive it. Additionally, Zenodo will create a DOI for your project and versioned DOIs for the project releases which can be added as a DOI badge. This makes it trivial for others to cite your work and allows you to indicate what version of your code was used in any publications.

## R Markdown in Jupyter with [jupytext](https://github.com/mwouts/jupytext)

[R Markdown](https://rmarkdown.rstudio.com/) is a very popular way to present beautifully rendered R along Markdown in different forms of documents. However, it is source only and not dynamically interactive as the R and Markdown needed to be [rendered together with Pandoc](https://stackoverflow.com/questions/40563479/relationship-between-r-markdown-knitr-pandoc-and-bookdown) ([Pandoc](https://pandoc.org/) is awesome).
> [jupytext](https://github.com/mwouts/jupytext) is a utility to open and run R markdown notebooks in Jupyter and save Jupyter notebooks as R markdown.

- [Install jupytext](https://github.com/mwouts/jupytext#installation)

Once you have installed jupytext create a Jupyter config with

```shell
jupyter notebook --generate-config
```

which creates the config file at

```
.jupyter/jupyter_notebook_config.py
```

Add the following line to the Jupyter config

```python
c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"
```

If you now launch a Jupyter notebook server and open a `.Rmd` file the R Markdown should now be rendered in the interactive environment of Jupyter!

### R Markdown in Jupyter in Binder

To get R Markdown working in Binder simple create a [`requirements.txt`](https://github.com/matthewfeickert/R-in-Jupyter-with-Binder/blob/master/binder/requirements.txt) file in the `binder` directory and add `jupytext` to it. Binder should take care of the rest!

- Here's a minimal example using the [`Example_Rmd.Rmd`](https://github.com/matthewfeickert/R-in-Jupyter-with-Binder/blob/master/Example_Rmd.Rmd) file from this repository: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/matthewfeickert/R-in-Jupyter-with-Binder/master?filepath=Example_Rmd.Rmd)

## Further Reading and Resources

- [Jupyter And R Markdown: Notebooks With R](https://www.datacamp.com/community/blog/jupyter-notebook-r), by [Karlijn Willems](https://github.com/Kacawi)
- [Rocker](https://www.rocker-project.org/)'s [R configurations for Docker repo](https://github.com/rocker-org/rocker)
- [Noam Ross](https://github.com/noamross), "[Docker for the UseR](https://github.com/noamross/nyhackr-docker-talk)", [New York Open Statistical Programming Meetup (nyhackr)](https://nyhackr.org/) (July 11th, 2018)
- [rOpenSci](https://ropensci.org/)

## Acknowledgements

- The [Jupyter and Binder team](https://github.com/orgs/jupyterhub/people) for making amazing open source software
- [Marc Wouts](https://github.com/mwouts) for creating [jupytext](https://github.com/mwouts/jupytext)
- [Achintya Rao](https://github.com/RaoOfPhysics) for insightful feedback, thoughtful discussion, and excellent ideas
