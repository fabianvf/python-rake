from __future__ import absolute_import
# Implementation of RAKE - Rapid Automtic Keyword Exraction algorithm
# as described in:
# Rose, S., D. Engel, N. Cramer, and W. Cowley (2010).
# Automatic keyword extraction from indi-vidual documents.
# In M. W. Berry and J. Kogan (Eds.), Text Mining: Applications and Theory.unknown: John Wiley and Sons, Ltd.

import re
import operator

__all__ = [
    'Rake',
    'SmartStopList',
    'FoxStopList',
    'MySQLStopList',
    'NLTKStopList',
    'GoogleSearchStopList',
    'RanksNLLongStopList',
]


def is_number(s):
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False


def SmartStopList():
    from .stoplists import SmartStopList
    return SmartStopList.words()


def FoxStopList():
    from .stoplists import FoxStopList
    return FoxStopList.words()


def MySQLStopList():
    from .stoplists import MySQLStopList
    return MySQLStopList.words()


def NLTKStopList():
    from .stoplists import NLTKStopList
    return NLTKStopList.words()


def GoogleSearchStopList():
    from .stoplists import GoogleSearchStopList
    return GoogleSearchStopList.words()


def RanksNLLongStopList():
    from .stoplists import RanksNLLongStopList
    return RanksNLLongStopList.words()


def RanksNLStoplist():
    from .stoplists import RanksNLStoplist
    return RanksNLStoplist.words()


def load_stop_words(stop_word_file, regex):
    with open(stop_word_file, encoding='utf8') as stop_word_file:
        stop_words = re.split(regex, stop_word_file.read())
    return [word for word in stop_words if word not in ('', ' ')]  # filters empty string matches


def separate_words(text):
    """
    Utility function to return a list of all words that are have a length greater than a specified number of characters.
    @param text The text that must be split in to words.
    @param min_word_return_size The minimum no of characters a word must have to be included.
    """
    splitter = re.compile('(?u)\W+')
    words = []
    for single_word in splitter.split(text):
        current_word = single_word.strip().lower()
        # leave numbers in phrase, but don't count as words, since they tend to invalidate scores of their phrases
        if current_word != '' and not is_number(current_word):
            words.append(current_word)
    return words


def split_sentences(text):
    """
    Utility function to return a list of sentences.
    @param text The text that must be split in to sentences.
    """
    sentence_delimiters = re.compile(u'[.!?,;:\t\\\\"\\(\\)\\\'\u2019\u2013]|\\s\\-\\s')
    sentences = sentence_delimiters.split(text)
    return sentences


def build_stop_word_regex(stop_word_list):
    stop_word_regex_list = []
    for word in stop_word_list:
        word_regex = r'\b' + word + r'(?![\w-])'
        stop_word_regex_list.append(word_regex)
    return re.compile('(?u)' + '|'.join(stop_word_regex_list), re.IGNORECASE)


def generate_candidate_keywords(sentence_list, stop_word_pattern, minCharacters, maxWords):
    phrase_list = []
    for s in sentence_list:
        tmp = re.sub(stop_word_pattern, '|', s.strip())
        phrases = tmp.split("|")
        for phrase in phrases:
            phrase = phrase.strip().lower()
            if phrase != '' and len(phrase) >= minCharacters and len(phrase.split()) <= maxWords:
                phrase_list.append(phrase)
    return phrase_list


def calculate_word_scores(phraseList):
    word_frequency = {}
    word_degree = {}
    for phrase in phraseList:
        word_list = separate_words(phrase)
        word_list_length = len(word_list)
        word_list_degree = word_list_length - 1
        for word in word_list:
            word_frequency.setdefault(word, 0)
            word_frequency[word] += 1
            word_degree.setdefault(word, 0)
            word_degree[word] += word_list_degree
    for item in word_frequency:
        word_degree[item] = word_degree[item] + word_frequency[item]

    # Calculate Word scores = deg(w)/frew(w)
    word_score = {}
    for item in word_frequency:
        word_score.setdefault(item, 0)
        word_score[item] = word_degree[item] / (word_frequency[item] * 1.0)
    return word_score


def generate_candidate_keyword_scores(phrase_list, word_score, minFrequency):
    keyword_candidates = {}
    for phrase in phrase_list:
        if phrase_list.count(phrase) >= minFrequency:
            keyword_candidates.setdefault(phrase, 0)
            word_list = separate_words(phrase)
            candidate_score = 0
            for word in word_list:
                candidate_score += word_score[word]
            keyword_candidates[phrase] = candidate_score
    return keyword_candidates


class Rake(object):

    def __init__(self, stop_words, regex='[\W\n]+'):
        #lets users call predefined stopwords easily in a platform agnostic manner or use their own list
        if isinstance(stop_words, list):
            self.__stop_words_pattern = build_stop_word_regex(stop_words)
        else:
            self.__stop_words_pattern = build_stop_word_regex(load_stop_words(stop_words, regex))

    def run(self, text, minCharacters=1, maxWords=5, minFrequency=1):
        sentence_list = split_sentences(text)

        phrase_list = generate_candidate_keywords(sentence_list, self.__stop_words_pattern, minCharacters, maxWords)

        word_scores = calculate_word_scores(phrase_list)

        keyword_candidates = generate_candidate_keyword_scores(phrase_list, word_scores, minFrequency)

        sorted_keywords = sorted(keyword_candidates.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_keywords
