import datetime
import pytz

local_tz = pytz.timezone('Europe/Madrid')


def get_current_datetime(dt: datetime) -> datetime:
    dt = dt.now(tz=local_tz)
    return dt


def get_local_datetime(dt: datetime) -> datetime:
    local_dt = dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)


def readable_datetime(dt: datetime) -> str:
    return dt.strftime("%d-%m-%Y %H:%M:%S")
