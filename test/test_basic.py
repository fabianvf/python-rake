import RAKE
from RAKE import Rake
from RAKE import SmartStopList


def test_instantiate():
    rake = Rake(SmartStopList())
    assert rake._Rake__stop_words_pattern
    rake = RAKE.Rake(RAKE.SmartStopList())
    assert rake._Rake__stop_words_pattern
