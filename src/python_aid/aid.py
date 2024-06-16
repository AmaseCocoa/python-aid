import time
import datetime
import sys

from python_aid import base36
import os

def get_noise() -> str:
    counter = int.from_bytes(os.urandom(2), 'little')
    return format(counter, 'x').zfill(2)[-2:]

def parseAid(aidx: str) -> datetime.datetime:
    """aidを生成します。

    Returns:
        str: aid
    """
    base36_time = aidx[:8]
    time_milliseconds = int(base36.b36decode(base36_time))
    timestamp = 946684800 + time_milliseconds / 1000
    if sys.version_info < (3, 11): # Python3.11からdatetimee.UTCが追加されたため
        return datetime.datetime.utcfromtimestamp(timestamp)
    return datetime.datetime.fromtimestamp(timestamp, datetime.UTC)

def genAid(timestamp: int=None) -> str:
    """aidを生成します。

    Returns:
        str: aid
    """
    if timestamp is None:
        timestamp = int((time.time() - 946684800) * 1000)
    base36_time = base36.b36encode(timestamp)
    noise = get_noise()
    aid = base36_time.zfill(8) + noise.zfill(2)
    return aid