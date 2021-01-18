# UInotebooks

## Diversity is considered a resource that enriches us culturally and intellectually in this class. No instances of harassment or attempts to marginalize students will be tolerated in my class. If you have concerns please come talk to me


This is a repo contains ALL code generated for [Principles of Urban Informatics Class at NYU CUSP Fall 2015-18](http://fbb.space/PUI2018/) for all the lectures taught by [FBB](http://fbb.space). 

(previous years: [2015 is here ](http://cosmo.nyu.edu/~fb55/UI_CUSP_2015))

For the current homework sets and labs go to [this](http://github.com/fedhere/PUI2018_fb55) Github repo.



This repo includes notebooks that will be explored in class, notebooks to be used as templates for lab sessions, and notebooks that generate plots used in the class, and class slides.

To run the notebooks, make sure that you have a directory for the plots, and outputs to be stored in, identified by environmental variables PUI2015, PUI15PLOTS, PUI2016 etc, as needed.

Numerous python packages are needed: numpy, scipy, sklearn, statsmodules, pandas. Mostly I try to be PEP8 compliant, but I am sloppy sometimes (while you should never be!). 

If you are a PUI student you may want to make a copy of this repository, and you definitely want to check for updates regularly.

If you just want to have your own copy of the repository on your machine what you want to do it __clone__ the repository on your machine as

```
git clone https://github.com/fedhere/UInotebooks.git
```
That way if I make changes you can update them locally on your machine with 

```
git pull
```

but you will not be able to make changes to my repository (as it should be).

Otherwise, if you want the repository on your account, with the ability to  make changes _to your own copy_, you can __fork__ the repository and have your own copy in your github account (it will be at http://github.com/<username>/PUI2018_fb55). In which case you want to _keep it synchronized_ following these instructions to [coniguting a remote for a fork](https://help.github.com/articles/configuring-a-remote-for-a-fork/) and [syncing a fork](https://help.github.com/articles/syncing-a-fork/)
 
 _If you see a mistake (there are many of course) and you want to propose a change you can submit a pull request, but be very clear about the change and it motivation in the description of your pull request, otherwise I will likely dismiss it as something you did accidentally._
 
The material here is for a class based on the following syllabus:

1.  

    Lecture: philosophy and good practices of data science: the flow chart of a data-driven project from idea to divulgation,  the concepts of falsifiability, reproducibility, open science, the importance of version control, iPython Notebooks
    Lab: command line tools. github repositories, setting up your environment, Python vs iPython, and iPython notebooks

2. 

    Lecture: acquiring and preparing data (CSV, TSV, downloadable ascii files, basic SQL) merging data from different files, plotting histograms and scatter plots, data types incl ordinal, continuous, categorical data
    Lab: read and clean data, Citibikes, Pluto, Census, introduction to data structures (dictionaries, lists, arrays), style guides

3.

    Lecture: Introduction to the statistics, why everything is gaussian (...or not), bias, basic distributions, moments, Hypothesis testing (chi-square, z-test, p-value)
    Lab: basic statistics on Pluto, Census, Citibikes data, moment extraction, deviations from gaussianity/poissonity, histograms, proper binning.

4.

    Lecture: PDF/CDF, data dredging, sample of 1, correlation vs causality, error analysis, testing models (KS, anderson darling, KL divergence), basic plotting.
    Lab: hypothesis testing

5.

    Lecture: Likelihood, OLS, WLS, basic bayesian concepts (maybe), missing data, small data, Unstructured data, API.
    Lab: goodness of fit, geopandas

6.

    Lecture: (time)-series  techniques: smoothing, detrending, stationary, non-stationary,  homeo- & hetero-scedastic noise, vectorization
    Lab: trash time series

7.	

    Lecture: Visualizations. Communication through visualizations, history, significance, good and bad visualization examples, what have we learnt since the 1800s?
    Lab: create a viz with pylab, small-multiples with pylab

8. 

    Guest Lecture: Data Hygiene
    Lab: Data Hygiene

9.

    Lecture:  Spatial+Temporal Urban data (multidimensional data), clustering. 
    Lab:  ZBP data

10. 

    Lecture: GeoPandas
    Lab: Geopandas
 		
11.

    Lecture: Spatial interpolation - Kriging
    
12. 

    Lecture: Trees

13.

    Lecture: Monte Carlo methods and MCMC


Missing Topics that could or should be included:

    optimization techniques (gradient descent, annealing...)
    designing experiments 
    web/mobile coding
    Audio vs Video data
    multiprocessing/multithreading
    Visualizations w D3
    NPL
    Graph Theory
    GIS 
    D3+GIS visualizations 



# PUI2018_fb55
