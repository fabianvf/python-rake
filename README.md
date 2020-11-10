python-rake
====

#### Note on Upgrades
Some users have reported issues importing the stoplists in the upgrade to 1.1.\*, if you experience import issues after upgrading try doing a full uninstall + reinstall.

---
![Build Status](https://github.com/fabianvf/python-rake/workflows/Python%20package/badge.svg)
![Upload Python Package](https://github.com/fabianvf/python-rake/workflows/Upload%20Python%20Package/badge.svg)
[![PyPI version](https://badge.fury.io/py/python-rake.svg)](https://badge.fury.io/py/python-rake)

A Python module implementation of the Rapid Automatic Keyword Extraction (RAKE) algorithm as described in: Rose, S., Engel, D., Cramer, N., & Cowley, W. (2010). Automatic Keyword Extraction from Individual Documents. In M. W. Berry & J. Kogan (Eds.), Text Mining: Theory and Applications: John Wiley & Sons. Initially by @aneesha, packaged by @tomaspinho.

The source code is released under the MIT License.

### Installation ###
    pip install python-rake #or pip3

### Usage ###
For external `.txt`, `.csv`, etc files:
Takes path as string datatype. Words can be on same or different lines but must be seperated by non-word characters. This should support all languages as it's based on unicode, but please validate the results of and report any issues with non-western languages, as they haven't been thoroughly tested.

    import RAKE
    Rake = RAKE.Rake(<path_to_your_stopwords_file>)
    Rake.run(<text>);

To change how a file is read-in, simply use the code below. The default regex described above is [\W\n]+.

    RAKE.Rake(<path_to_your_stopwords_file> , regex = '<your regex>')

For lists:

    import RAKE
    Rake = RAKE.Rake(<list>); #takes stopwords as list of strings
    Rake.run(<text>)

`SmartStopList()`, `FoxStopList()`, `NLTKStopList()` and `MySQLStopList` return the expected lists as lists, they can be used as shown bellow. `GoogleSearchStopList()` returns what were thought to be stop words in Google search back when large numbers of search suggestions very available. `RanksNLStopList()` and `RanksNLLongStopList()` returns the in-house developed stoplists from Ranks NL, a webmaster suite.

    import RAKE
    Rake = RAKE.Rake(RAKE.SmartStopList())
    Rake.run(<text>)

Additional flags:

The RAKE.rake function also accepts minCharacters, maxWords and minFrequency flags to better tune your outputs. minCharacters is the minimum characters allowed in a keyword. maxWords is the maximum number of words allowed in a phrase considered as a keyword. minFrequency is the minimum number of occurances a keyword has to have to be considered as a keyword. An example of this which shows the default values is as follows:

    import RAKE
    rake = RAKE.Rake(RAKE.SmartStopList())
    rake.run(<text>, minCharacters = 1, maxWords = 5, minFrequency = 1)

Other stoplists and stoplists in other languages can be found at https://github.com/trec-kba/many-stop-words/tree/master/orig, at http://www.ranks.nl/stopwords, at https://sites.google.com/site/kevinbouge/stopwords-lists and in the NLTK stopwords package

### Releases ###
I will push releases to PyPi periodically, but if there is a feature in master not built/pushed and you want it to be, just ping me.

### Credit ###
This is a maintained fork of the original python RAKE project, which can be found here: https://github.com/aneesha/RAKE
The Fox Stopwords list was originally created by Christopher Fox, http://dl.acm.org/citation.cfm?id=378888
The Smart stopwords list was originally created by Gerard Salton and Chris Buckley for the experimental SMART information retrieval system at Cornell University.
The MySQL stopwords list is (surprisingly) from MySQL, owned and mainted by Oracle and under the GPL2 license.
The NTLK stopword list was created by the NLTK project under the Apache license, project here: https://github.com/nltk/nltk
The Ranks NL stopword lists were created by Ranks NL, who also compiled the Google Search stopword list, who said via email that we could include them in this package if we credited them.
