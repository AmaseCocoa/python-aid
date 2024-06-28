import datetime
import random
import sys
import time

from . import base36


def genAidx(timestamp: float=None) -> str:
    """aidxを生成します。

    Returns:
        str: aidx
    """
    if timestamp is None:
        timestamp = int((time.time() - 946684800) * 1000)
        # raise NotImplementedError("The function to generate aidx from timestamp is currently not available due to incompatibility with Misskey's aidx :(")
    else:
        timestamp = int((timestamp - 946684800) * 1000)
    base36_time = base36.encode(timestamp)
    individual_id = '{:04X}'.format(random.randint(0, 65535))
    counter = '{:04X}'.format(random.randint(0, 65535))
    aidx = base36_time.zfill(8) + individual_id.zfill(4) + counter.zfill(4)
    return aidx

def parseAidx(aidx) -> datetime.datetime:
    """aidxをdatetime形に変換します。

    Args:
        aidx (str): aidx

    Returns:
        datetime.datetime: _description_
    """
    base36_time = aidx[:8]
    time_milliseconds = int(base36.decode(base36_time))
    timestamp = 946684800 + time_milliseconds / 1000
    if sys.version_info < (3, 11): # Python3.11からdatetimee.UTCが追加されたため
        return datetime.datetime.utcfromtimestamp(timestamp)
    return datetime.datetime.fromtimestamp(timestamp, datetime.UTC)