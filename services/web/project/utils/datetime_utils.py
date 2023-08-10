import ctypes as c
import datetime
import pytz

_get_dict = c.pythonapi._PyObject_GetDictPtr
_get_dict.restype = c.POINTER(c.py_object)
_get_dict.argtypes = [c.py_object]

local_tz = pytz.timezone('Europe/Madrid')


def get_current_date_time() -> datetime:
    dt = datetime.now(tz=local_tz)
    print(dt.strftime("%d-%m-%Y %H:%M:%S"))
    return dt


def get_local_date_time(date: datetime) -> datetime:
    local_dt = date.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)


d = _get_dict(datetime.datetime)[0]
d['get_current_date_time'] = get_current_date_time
d['get_local_date_time'] = get_local_date_time
