import datetime as dt
import time
import pytz
import os


"""
     "The concept of waiting bewilders me. There are always
     deadlines. There are always ticking clocks. That's why
                                 you must manage your time"

                                                - Whiterose

"""

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y/%m/%d"
TIME_FORMAT = "%H:%M:%S"
TIMEZONES = {
    "MX": "Mexico/General",
    "UTC": "Universal"
}

"""
    localtime() = time.struct_time
    today('UTC|MX') UTC = 2020/12/18T22:24:58
                    MX = 2020/12/18T16:24:58
"""

def localtime():

    """ Returns struct_time """

    return time.localtime(time.time())


def today(tz="Universal"):

    """ Get current datetime. Timezone aware

    Keyword Arguments:
        tz {str} -- [description] (default: {"UTC"})

    Returns:
        {str} Datetime string, format %Y/%m/%dT%H:%M:%S

        today(UTC) = 2020/12/18T22:01:45
        today(MX) = 2020/12/18T16:01:45
    """

    tzdt = dt.datetime.now(pytz.timezone(tz))
    return dt.datetime.strftime(tzdt, DATETIME_FORMAT)


class Epoch:

    """ Unix time manager class """

    timezone = "Universal"

    """
    Epoch.dump(2020, 12, 18, 16) = 1608328800.0
    Epoch.load(epoch) = 2020-12-18 16:24:58.109826 Type: <class 'datetime.datetime'>
    Epoch.now()=1608330298.110156 Type: <class 'float'>
    Epoch.strfload(epoch, datetime=True|False) T = 2020/12/18T16:24:58
                                               F = 2020/12/18 Type: <class 'str'>
    """

    @classmethod
    def dump(cls, year, month, day, hr=0, mins=0, sec=0, msec=0, tz=None):

        """ Dump unix timestamp (EPOCH)
        """

        dtt = dt.datetime(year, month, day, hr, mins, sec, msec,
                          tzinfo=pytz.timezone(cls.timezone))
        if bool(tz):
            dtt = dtt.astimezone(pytz.timezone(tz))

        dtt = dt.datetime.strptime(dtt.strftime(DATETIME_FORMAT), DATETIME_FORMAT)
        return dtt.timestamp()

    @classmethod
    def now(cls, tz=None):

        """ Returns current datetime epoch. Timezone aware

        Returns:
            <class 'float'>
        """
        tzinfo = tz if bool(tz) else cls.timezone
        tgt_timezone = pytz.timezone(tzinfo)
        dtime = dt.datetime.now(tgt_timezone)
        return dtime.timestamp()

    @classmethod
    def load(cls, epoch, only_date=False, only_time=False):

        """ load datetime from unix timestamp

        Arguments:
            epoch <class 'float'> -- Unix timestamp e.g. 1608328905.92277

        Returns:
            string - (date[time]|time)
        """
        dt_format = DATE_FORMAT if only_date else DATETIME_FORMAT
        dt_format = TIME_FORMAT if only_time else dt_format
        dtt = dt.datetime.fromtimestamp(epoch)
        return dtt.strftime(DATETIME_FORMAT)