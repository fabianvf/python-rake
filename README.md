python-rake
====

[![Build Status](https://travis-ci.org/fabianvf/python-rake.svg?branch=master)](https://travis-ci.org/fabianvf/python-rake)

A Python module implementation of the Rapid Automatic Keyword Extraction (RAKE) algorithm as described in: Rose, S., Engel, D., Cramer, N., & Cowley, W. (2010). Automatic Keyword Extraction from Individual Documents. In M. W. Berry & J. Kogan (Eds.), Text Mining: Theory and Applications: John Wiley & Sons. Initially by @aneesha, packaged by @tomaspinho.

The source code is released under the MIT License.

### Installation ###
    pip install python-rake

### Usage ###
#for external .txt files
    import RAKE
    Rake = RAKE.Rake(<path_to_your_stopwords_file>);
    Rake.run(text);
#for built in stoplists
    import RAKE
    Rake = RAKE.Rake(<keyword>); #current keywords are SmartStopList and FoxStopList
    Rake.run(text);

### Credit ###
This is a maintained fork of the original python RAKE project, which can be found here: https://github.com/aneesha/RAKE
