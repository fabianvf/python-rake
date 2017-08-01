try:
    from RAKE import Rake, SmartStopList, FoxStopList, MySQLStopList, NLTKStopList # NOQA
except ImportError:
    from RAKE.RAKE import Rake, SmartStopList, FoxStopList, MySQLStopList, NLTKStopList # NOQA
