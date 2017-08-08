python-rake
====

#### Note on Upgrades
Some users have reported issues importing the stoplists in the upgrade to 1.1.\*, if you experience import issues after upgrading try doing a full uninstall + reinstall. 

---

[![Build Status](https://travis-ci.org/fabianvf/python-rake.svg?branch=master)](https://travis-ci.org/fabianvf/python-rake)

A Python module implementation of the Rapid Automatic Keyword Extraction (RAKE) algorithm as described in: Rose, S., Engel, D., Cramer, N., & Cowley, W. (2010). Automatic Keyword Extraction from Individual Documents. In M. W. Berry & J. Kogan (Eds.), Text Mining: Theory and Applications: John Wiley & Sons. Initially by @aneesha, packaged by @tomaspinho.

The source code is released under the MIT License.

### Installation ###
    pip install python-rake #or pip3

### Usage ###
For external `.txt`, `.csv`, etc files:
take path as string datatype. words can be on same or different lines but must be seperated by non-word characters

    import RAKE
    Rake = RAKE.Rake(<path_to_your_stopwords_file>)
    Rake.run(text);

Changing file read-in:

By default, words on each line will be broken appart by \W+ in regex. This means non-word characters (commas, slashes, spaces, dashes, periods etc.), included removing trailing ones, repeated ones, and dissimilar ones. *This means that single-line lists work fine along with multi-line lists*. This should support all languages as it's based on unicode, but please validate the results of and report any issues with non-western languages.

To stop lines being divided, use the flag `divide=False`. To use a delimiter character other than non-word characters, use the flag `delimiter = <regex flag of your choosing as string>`, which is ignored if used with `divide = False`. 

For lists:

    import RAKE
    Rake = RAKE.Rake(<list>); #takes stopwords as list of strings
    Rake.run(text)

`RAKE.SmartStopList()`, `RAKE.FoxStopList()`, `NLTKStopList()` and `MySQLStopList` return the expected lists as lists, they can be used as shown bellow:

    import RAKE
    Rake = RAKE.Rake(RAKE.SmartStopList())
    Rake.run(text)

Other stoplists and stoplists other languages can be found at https://github.com/trec-kba/many-stop-words/tree/master/orig, at http://www.ranks.nl/stopwords and in the NLTK stopwords package
    
### Releases ###
I will push releases to pypi periodically, but if there is a feature in master not built/pushed and you want it to be, just ping me.
 
### Credit ###
This is a maintained fork of the original python RAKE project, which can be found here: https://github.com/aneesha/RAKE
The Fox Stopwords list was originally created by Christopher Fox, http://dl.acm.org/citation.cfm?id=378888
The Smart stopwords list was originally created by Gerard Salton and Chris Buckley for the experimental SMART information retrieval system at Cornell University.
The MySQL stopwords list is (surprisingly) from MySQL, owned and mainted by Oracle and under the GPL2 license.
The NTLK stopword list was created by the NLTK project under the Apache license, project here: https://github.com/nltk/nltk

