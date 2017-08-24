#from http://www.ranks.nl/stopwords , copy of permission granting here https://github.com/fabianvf/python-rake/issues/20

#based on suspected stopwords from analyzing displayed google search suggestions before they had to remove them over
#people making lists like this (or "why we can't have nice things)

wordlist = [
    "a",
    "about",
    "an",
    "are",
    "as",
    "at",
    "be",
    "by",
    "com",
    "for",
    "from",
    "how",
    "i",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "the",
    "this",
    "to",
    "was",
    "what",
    "when",
    "where",
    "who",
    "will",
    "with",
    "www"
]


def words():
    return wordlist
