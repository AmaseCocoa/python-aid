import datetime
import os
import sys
import time

from python_aid import base36


def getNoise() -> str:
    counter = int.from_bytes(os.urandom(2), 'little')
    return format(counter, 'x').zfill(2)[-2:]

def parseAid(aidx: str) -> datetime.datetime:
    """aidを生成します。

    Returns:
        str: aid
    """
    base36_time = aidx[:8]
    time_milliseconds = int(base36.decode(base36_time))
    timestamp = 946684800 + time_milliseconds / 1000
    if sys.version_info < (3, 11): # Python3.11からdatetimee.UTCが追加されたため
        return datetime.datetime.utcfromtimestamp(timestamp)
    return datetime.datetime.fromtimestamp(timestamp, datetime.UTC)

def genAid(timestamp: float=None) -> str:
    """aidを生成します。

    Returns:
        str: aid
    """
    if timestamp is None:
        timestamp = int((time.time() - 946684800) * 1000)
        # raise NotImplementedError("The function to generate aid from timestamp is currently not available due to incompatibility with Misskey's aid :(")
    else:
        timestamp = int((timestamp - 946684800) * 1000)
    base36_time = base36.encode(timestamp)
    noise = getNoise()
    aid = base36_time.zfill(8) + noise.zfill(2)
    return aid