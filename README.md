python-rake
====

#### Note on Upgrades
Some users have reported issues importing the stoplists in the upgrade to 1.1.\*, if you experience import issues after upgrading try doing a full uninstall + reinstall. 

---

[![Build Status](https://travis-ci.org/fabianvf/python-rake.svg?branch=master)](https://travis-ci.org/fabianvf/python-rake)

A Python module implementation of the Rapid Automatic Keyword Extraction (RAKE) algorithm as described in: Rose, S., Engel, D., Cramer, N., & Cowley, W. (2010). Automatic Keyword Extraction from Individual Documents. In M. W. Berry & J. Kogan (Eds.), Text Mining: Theory and Applications: John Wiley & Sons. Initially by @aneesha, packaged by @tomaspinho.

The source code is released under the MIT License.

### Installation ###
    pip install python-rake

### Usage ###
for external .txt files
take path as string datatype. words can be on same or different lines but must be seperated by spaces.

    import RAKE
    Rake = RAKE.Rake(<path_to_your_stopwords_file>); 
    Rake.run(text);

for lists:

    import RAKE
    Rake = RAKE.Rake(<list>); #takes stopwords as list of strings
    Rake.run(text);

`RAKE.SmartStopList()` and `RAKE.FoxStopList()` return the expected lists as lists, they can be used as shown bellow:
    
#### Additional Parameters ####

```python
    import RAKE
    Rake = RAKE.Rake(
        stopwords,
        min_char_length=1, # minimum number of characters each word should have
        max_words_length=5, # maximum number of words each phrase should have
        min_keyword_frequency=1 # minimum number of times each keyword should appear
    )
```


### Releases ###
I will push releases to pypi periodically, but if there is a feature in master not built/pushed and you want it to be, just ping me.
 
### Credit ###
This is a maintained fork of the original python RAKE project, which can be found here: https://github.com/aneesha/RAKE
